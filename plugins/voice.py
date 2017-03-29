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
        return {'name': 'voice', 
                'title': 'Voice Synth', 
                'description': 'A text-to-speech synthesizer.', 
                'version': 1.0}

    @property
    def response(self):
        return None

    def respond(self):
        if self.response:
            pass
        else:
            pass