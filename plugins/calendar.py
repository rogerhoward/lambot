import requests


class Action(object):
    payload = None
    response_type = 'ephemeral'

    def __init__(self, payload):
        print('loading calendar with', payload)
        self.payload = payload
        self.respond()

    @property
    def info(self):
        return {'name': 'calendar', 
                'title': 'Calendar of Events', 
                'description': 'Calendar of Events', 
                'version': 1.0}

    @property
    def response(self):
        return {'text': 'echo:' + self.payload.get('text'), 'response_type': self.response_type}

    def respond(self):
        if self.response:
            requests.post(self.payload.get('url'), data = self.response)
        else:
            pass