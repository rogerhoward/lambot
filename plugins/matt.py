import requests
import json


class Action(object):
    payload = None
    response_type = 'in_channel'

    def __init__(self, payload):
        print('loading matt plugin with', payload)
        self.payload = payload
        self.respond()

    @property
    def info(self):
        return {'name': 'matt', 
                'title': 'Tell Off Matt', 
                'description': 'Tell Matt to Stuffit', 
                'version': 1.0}

    def respond(self):
        url = self.payload.get('response_url')
        if url:
            response_payload = {'text': 'Shutup, woulda yah?', 'response_type': self.response_type}
            requests.post(url, json=response_payload)