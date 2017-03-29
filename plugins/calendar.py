    
class Action(object):
    payload = None

    def __init__(self):
        print('initializing calendar')

    @property
    def info(self):
        return {'name': 'calendar', 
                'title': 'Calendar of Events', 
                'description': 'Calendar of Events', 
                'version': 1.0}

    def load(self, payload):
        print('loading calendar with', payload)
        self.payload = payload
        return True

    @property
    def response(self):
        return self.payload.get('text')