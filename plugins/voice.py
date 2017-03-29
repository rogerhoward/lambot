
class Action(object):
    payload = None

    def __init__(self):
        print('initializing voice')

    @property
    def info(self):
        return {'name': 'voice', 
                'title': 'Voice Synth', 
                'description': 'A text-to-speech synthesizer.', 
                'version': 1.0}

    @property
    def load(self, payload):
        print('loading voice with', payload)
        self.payload = payload
        return False

    @property
    def response(self):
        return self.payload.get('text')