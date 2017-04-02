import requests
import json
# from ..plugins import SimpleAction

class Action(object):

    channels = ['bot', ]

    payload = None
    response_type = 'ephemeral'

    def __init__(self, payload):
        print('loading calendar with', payload)
        self.payload = payload
        
        if self.channels and self.payload['channel'] in self.channels:
            try:
                self.respond()
            except:
                print('plugin {} failed. WTF.'.format(self.info['name']))

    @property
    def info(self):
        return {'name': 'calendar', 
                'title': 'Calendar of Events', 
                'description': 'Calendar of Events', 
                'version': 1.0}

    def respond(self):
        message = 'echo: {}'.format(self.payload.get('text'))
        url = self.payload.get('response_url')
        print(message, url)
        if url:
            response_payload = {'text': message, 'response_type': self.response_type}
            requests.post(url, json=response_payload)