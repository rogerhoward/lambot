import requests
import json
import random
import datetime
import arrow
from action import SimpleAction
import config

import os
import io
import boto3
from PIL import Image, ImageDraw


class Fractal(object):
    def __init__(self, width, height, iterations):
        self.width = width
        self.height = height
        self.iterations = iterations

        self.filename = '{}x{}_{}.png'.format(width, height, iterations)
        print(self.filename)

        self.url = None

        self.image = Image.new("RGB", (width, height))
        self.draw = ImageDraw.Draw(self.image)

        self.s3 = boto3.client('s3')


class Mandelbrot(Fractal):
    def __init__(self, width, height, iterations):
        super(Mandelbrot, self).__init__(width, height, iterations)

    def __repr__(self):
        return 'Mandelbrot({}, {}, ({}))'.format(self.width, self.height, self.iterations)

    def putpixel(self, col, row, color):
        self.draw.point((col, row), fill = color)
        return True

    def get_color(self, index):
        if index < self.iterations:
            return (255, 255, 255)
        else:
            return (0, 0, 0)

    def render(self):
        print('rendering...')
        for row in range(self.height):
            for col in range(self.width):
                # print(col, row)

                c_re = (col - self.width / 2.0) * 4.0 / self.width
                c_im = (row - self.height / 2.0) * 4.0 / self.width
                x = 0
                y = 0

                iteration = 0

                while (x * x + y * y) <= 4 and iteration < self.iterations:
                    x_new = x * x - y * y + c_re
                    y = 2 * x * y + c_im
                    x = x_new
                    iteration += 1

                self.putpixel(col, row, self.get_color(iteration))
        return self

    def show(self):
        self.image.show()
        return self

    def bytesio(self):
        image_bytes = io.BytesIO()
        self.image.save(image_bytes, 'PNG')
        image_bytes.seek(0)
        return image_bytes

    def upload(self):
        print('uploading...')
        self.s3.put_object(Bucket='lambot-fractals', Key=self.filename, Body=self.bytesio())
        self.url = 'https://s3.amazonaws.com/lambot-fractals/{}'.format(self.filename)
        return self



class Action(SimpleAction):
    name = 'fractal'
    title = 'Generates fractals'
    description = 'Creates random fractals in the Mandelbrot or Julia sets.'
    version = 0.1
    help_command = 'fractal help'
    help_string = '"/lambot fractal" will create a random fractal image.\n"/lambot fractal [mandelbrot,julia]" will draw the given set'

    channels = '*'

    payload = None
    # response_type = 'in_channel'


    def check(self):
        if self.text.startswith('fractal'):
            print('fractal active and responding...')
            return True
        else:
            print('fractal not responding...')
            return False


    def response(self):
        this_fractal = Mandelbrot(600, 400, 50)
        this_fractal.render().upload()

        fractal_attachment = {'image_url': this_fractal.url, 'fallback': str(this_fractal), 'title': str(this_fractal)}
        response_payload = {'text': 'A fractal for you: {}'.format(this_fractal), 'attachments': [fractal_attachment], 'response_type': self.response_type}

        return response_payload