import requests
import json
from action import SimpleAction
import config

class Action(SimpleAction):
    name = 'calendar'
    title = 'Calendar of Events'
    description = 'Calendar of Events'
    version = 0.1

    feed = 'https://www.meetup.com/code-and-coffee-long-beach/events/atom/'

    def __init__(self, payload):
        self.payload = payload
        print('preparing to load calendar...')
        if self.in_channel() and self.check():
            # try:
            self.respond()

    def in_channel(self):
        return True

    def check(self):
        command = self.payload.get('text', '')
        print('command:', command)
        if command.startswith('calendar'):
            print('calendar active and responding...')
            return True
        else:
            print('calendar not responding...')
            return False


    def response(self):

        url = 'https://api.meetup.com/2/events'
        data = {'offset': 0, 'page': 20, 'format': 'json', 'limited_events': 'False', 'group_urlname': 'code-and-coffee-long-beach', 'photo-host': 'public', 'status':'upcoming', 'key': config.MEETUP_KEY, 'order': 'time', 'desc': 'false', 'fields': ''}

        meetups = requests.get(url, params=data).json().get('results', [])

        if len(meetups) > 0:
            next_meet = meetups[1]
            venue = next_meet['venue']
            message = 'The next Meetup is at {name}, located at {address_1}, {city}, {state}'.format(**venue)

            location_escaped = '{address},+{city},+{state}'.format(**{'address': venue['address_1'].replace(' ', '+'), 'city': venue['city'].replace(' ', '+'), 'state': venue['state'].replace(' ', '+')})
            map_image = 'https://maps.googleapis.com/maps/api/staticmap?center={location}&zoom=15&scale=2&size=400x400&maptype=roadmap&format=png&visual_refresh=true&markers=size:mid%7Ccolor:0xff0000%7Clabel:1%7C{location}'.format(**{'location': location_escaped})

            attachment = {'title': 'Next meetup', 'text': message, 'image_url': map_image}

            if self.payload.get('response_url'):
                response_payload = {'text': message, 'response_type': self.response_type, 'attachments': [attachment]}
                return response_payload
            else:
                return None
        else:
            return None


    def respond(self):
        response = self.response()
        url = self.payload.get('response_url')
        if response and url:
            requests.post(url, json=response)