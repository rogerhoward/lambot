import requests
import json
import datetime
import arrow
from action import SimpleAction
import config


class Action(SimpleAction):
    name = 'help'
    title = 'Lambot Help'
    description = 'Lists available plugins and their descriptions.'
    version = 0.1


    def in_channel(self):
        return True

    def check(self):
        if self.text.lower() == 'help':
            print('help plugin activated..')
            return True
        else:
            print('help plugin ignored...')
            return False


    def response(self):
        # Create Slack response payload
        response_payload = {'text': ', '.join(plugin_names), 'response_type': self.response_type}
        return response_payload
