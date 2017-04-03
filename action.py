import requests


class SimpleAction(object):
    response_type = 'ephemeral'  # Set to 'ephemeral' to respond in private, and 'in_channel' to respond publicly 
    channels = ['bot', ]  # Set to '*' to listen on all channels, or list the channels your plugn should listen to

    # Metadata about your plugin
    name = None  # A shortname for your plugin; should correspond to your Python filename without the .py
    title = None  # The formal name for your plugin
    description = None  # A lengthier description of your plugin
    version = None  # A version number, if you care.
    help_command = None
    help_string = None

    def __init__(self, payload, context):
        self.context = context
        self.payload = payload  # Stash a reference to class instance in the base class
        self._apply_payload(payload)  # Expose payload values as instance properties

        # If plugins (and not just being dry-loaded) and has payload and context
        if context.get('active', False) and payload and context:

            # If this is a plugin help command...
            if self.text == self.help_command:
                self.help()

            # If this command is in the right channel and passes other checks...
            elif self.in_channel() and self.check():
                print('about to use plugin {}...'.format(self.title))
                self.respond()

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
        if payload:
            self.token = payload.get('token', None)
            self.team_id = payload.get('team_id', None)
            self.team_domain = payload.get('team_domain', None)
            self.channel_id = payload.get('channel_id', None)
            self.channel_name = payload.get('channel_name', None)
            self.user_id = payload.get('user_id', None)
            self.user_name = payload.get('user_name', None)
            self.command = payload.get('command', None)
            self.text = payload.get('text', None)
            self.response_url = payload.get('response_url', None)


    def in_channel(self):
        """
        Did the command come in on a channel this plugin is listening to?
        """
        if self.channels:
            if self.channels == '*':
                return True
            elif self.channel_name in self.channels:
                return True
            else:
                return True
        else:
            return False

    def check(self):
        """ 
        Should this plugin be activated?
        """
        raise NotImplementedError

    def respond(self):
        """
        Unwraps values from payload and applies them to the class instance as properties
        """
        response = self.response()
        if response and self.response_url:
            requests.post(self.response_url, json=response)

    def response(self):
        """
        Returns the response dictionary for the current payload.
        This should only be run after passing check()
        The response format is documented at https://api.slack.com/slash-commands#responding_to_a_command
        """
        raise NotImplementedError

    def help(self):
        """
        Returns a help message for this command.
        """
        if self.response_url:
            response_payload = {'text': self.help_string, 'response_type': 'ephemeral'}
            requests.post(self.response_url, json=response_payload)