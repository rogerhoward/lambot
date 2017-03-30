import requests
import json


class Action(object):
    payload = None
    response_type = 'in_channel'

    def __init__(self, payload):
        print('loading matt plugin with', payload)
        self.payload = payload

        try:
            if self.payload.get('text')[0:4].lower() == 'matt':
                self.respond()
        except:
            print('plugin {} failed. WTF.'.format(self.info['name']))

    @property
    def info(self):
        return {'name': 'matt', 
                'title': 'Tell Off Matt', 
                'description': 'Tell Matt to Stuffit', 
                'version': 1.0}

    def respond(self):
        url = self.payload.get('response_url')
        if url:
            response_payload = {'text': 'Shutup, would yah?', 'response_type': self.response_type}
            requests.post(url, json=response_payload)