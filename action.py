
class SimpleAction(object):
    response_type = 'ephemeral'
    channels = ['bot', ]

    name = None
    title = None
    description = None
    version = None

    def __init__(self, payload):
        self.payload = payload

        if self.in_channel() and self.check():
            # try:
            self.respond()
            # except:
                # print('plugin {} failed. WTF.'.format(self.info['name']))

    @property
    def info(self):
        return {'name': self.name, 
                'title': self.title, 
                'description': self.description, 
                'version': self.version}

    def in_channel(self):
        if self.channels is None:
            return True
        elif self.payload.get('channel') in self.channels:
            return True
        else:
            return False

    def check(self):
        return False

    def respond(self):
        pass

    def response(self):
        pass