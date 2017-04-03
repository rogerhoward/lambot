import plugins

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
    help_command = 'help help'
    help_string = '"/help" will respond with information about available commands.'


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
        # plugin_names = [x['name'] for x in self.context['plugins']]

        message = []
        for this_plugin in self.context['plugins']:
            plugin_message = '{} (/lambot {})\n{}\n"/lambot {} help" for more detailed help'.format(this_plugin['title'], this_plugin['name'], this_plugin['description'], this_plugin['name'])
            print(plugin_message)
            message.append(plugin_message)

        response_payload = {'text': '\n----------\n'.join(message), 'response_type': self.response_type}
        return response_payload
