
class SimpleAction(object):
    response_type = 'ephemeral'
    payload = {}
    channels = ['bot', ]

    name = None
    title = None
    description = None
    version = None

    def __init__(self, instance, payload):
        self._apply_payload(instance, payload)

        print('preparing to load {}...'.format(instance.title))
        if instance.in_channel() and instance.check():
            # try:
            instance.respond()
            # except:
                # print('plugin {} failed. WTF.'.format(self.info['name']))

    @property
    def info(self):
        return {'name': self.name, 
                'title': self.title, 
                'description': self.description, 
                'version': self.version}

    def _apply_payload(self, instance, payload):
        instance.token = payload.get('token', None)
        instance.team_id = payload.get('team_id', None)
        instance.team_domain = payload.get('team_domain', None)
        instance.channel_id = payload.get('channel_id', None)
        instance.channel_name = payload.get('channel_name', None)
        instance.user_id = payload.get('user_id', None)
        instance.user_name = payload.get('user_name', None)
        instance.command = payload.get('command', None)
        instance.text = payload.get('text', None)
        instance.response_url = payload.get('response_url', None)


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