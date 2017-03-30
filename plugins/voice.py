import requests
import json

class Action(object):
    payload = None
    response_type = 'ephemeral'

    def __init__(self, payload):
        print('loading voice with', payload)
        self.payload = payload

        try:
            self.respond()
        except:
            print('plugin {} failed. WTF.'.format(self.info['name']))

    @property
    def info(self):
        return {'name': 'voice', 
                'title': 'Voice Synth', 
                'description': 'A text-to-speech synthesizer.', 
                'version': 1.0}

    def respond(self):
        pass

