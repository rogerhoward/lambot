import requests


class SimpleAction(object):
    response_type = 'ephemeral'
    channels = ['bot', ]

    name = None
    title = None
    description = None
    version = None

    def __init__(self, instance, payload):
        self.instance = instance  # Stash a reference to class instance in the base class
        self._apply_payload(payload)  # Expose payload values as instance properties

        print('preparing to load {}...'.format(instance.title))

        if instance.in_channel() and instance.check():
            instance.respond()

    @property
    def info(self):
        """
        Returns a dictionary of metadata about the class instance
        """
        return {'name': self.name, 
                'title': self.title, 
                'description': self.description, 
                'version': self.version}

    def _apply_payload(self, payload):
        """
        Unwraps values from payload and applies them to the class instance as properties
        """
        self.instance.payload = payload

        self.instance.token = payload.get('token', None)
        self.instance.team_id = payload.get('team_id', None)
        self.instance.team_domain = payload.get('team_domain', None)
        self.instance.channel_id = payload.get('channel_id', None)
        self.instance.channel_name = payload.get('channel_name', None)
        self.instance.user_id = payload.get('user_id', None)
        self.instance.user_name = payload.get('user_name', None)
        self.instance.command = payload.get('command', None)
        self.instance.text = payload.get('text', None)
        self.instance.response_url = payload.get('response_url', None)


    def in_channel(self):
        """
        Should this plugin be activated for the payload, based the channel?
        """
        return True

    def check(self):
        """
        Should this plugin be activated?
        """
        return False

    def respond(self):
        """
        Unwraps values from payload and applies them to the class instance as properties
        """
        response = self.instance.response()
        if response and self.instance.response_url:
            requests.post(self.instance.response_url, json=response)

    def response(self):
        """
        Returns the response dictionary for the current payload.
        This should only be run after passing check()
        """
        return None