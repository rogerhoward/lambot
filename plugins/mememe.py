import requests
import json
import random
import datetime
import arrow
from action import SimpleAction
import config

class Action(SimpleAction):
    name = 'mememe'
    title = 'Generates Memes'
    description = 'Creates random memes, using random meme images.'
    version = 0.1
    help_command = 'mememe help'
    help_string = '"/lambot mememe" will grab a random meme image.\n"/lambot mememe message" will caption a random meme image with *message*'

    channels = '*'

    payload = None
    response_type = 'in_channel'


    def check(self):
        if self.text.startswith('mememe'):
            print('mememe active and responding...')
            return True
        else:
            print('mememe not responding...')
            return False


    def response(self):
        r = requests.get('https://api.imgflip.com/get_memes')
        memes = r.json().get('data', {}).get('memes', [])
        if len(memes) > 0:
            random_meme = random.choice(memes)

            if self.text == 'mememe':
                meme_attachment = {'image_url': random_meme['url'], 'fallback': random_meme['name'], 'title': random_meme['name']}
            else:
                caption = self.text[7:]
                custom_meme = requests.post('https://api.imgflip.com/caption_image', data = {'template_id': random_meme['id'], 'username': 'imgflip_hubot', 'password': 'imgflip_hubot', 'text0': caption}).json()

                meme_attachment = {'image_url': custom_meme['data']['url'], 'fallback': random_meme['name'], 'title': random_meme['name']}

            response_payload = {'text': 'Your hot, fresh meme:', 'attachments': [meme_attachment], 'response_type': self.response_type}
        
        else:
            response_payload = {'text': 'Something went wrong with mememe!', 'response_type': 'ephemeral'} 

        return response_payload