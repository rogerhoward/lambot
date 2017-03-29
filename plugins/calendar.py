
class Action(object):
    payload = {}

    def __init__(self, payload):
        self.payload = payload
        print('initializing calendar with', self.payload)

    @property
    def valid(self):
        return True

    @property
    def response(self):
        return self.payload.get('text')