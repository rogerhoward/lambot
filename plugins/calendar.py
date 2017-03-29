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

    # @property
    # def response(self):
    #     return {'text': 'echo:' + self.payload.get('text'), 'response_type': self.response_type}

    def respond(self):
        message = 'echo: {}'.format(self.payload.get('text'))
        response = {'text': message, 'response_type': self.response_type}
        requests.post(self.payload.get('response_url'), data=response)