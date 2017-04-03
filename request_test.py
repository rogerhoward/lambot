#!/usr/bin/env python
import os
import requests
from pprint import pprint
import click

@click.command()
@click.option('--token', default='gIkuvaNzQIHg97ATvDxqgjtO', help='Slack API token.')
@click.option('--team_id', default='T0001', help='The unique Slack team ID')
@click.option('--team_domain', default='example', help='The unique Slack domain')
@click.option('--channel_id', default='C2147483705', help='The unique ID of the channel where this command originated')
@click.option('--channel_name', default='bot', help='The name of the channel where this command originated')
@click.option('--user_id', default='U2147483697', help='The unique ID of the user who sent this command')
@click.option('--user_name', default='rogerhoward', help='The username of the user who sent this command.')
@click.option('--command', default='/lambot', help='The slash command name')
@click.option('--text', default='calendar', help='All text that followed the slash command - generally options and modifiers')
@click.option('--response_url', default='http://0.0.0.0:5000/test/response', help='The URL where to POST the response(s) - up to five responses may be POSTed to this Webhook')
@click.option('--url', default='http://0.0.0.0:5000/', help='The URL where to POST the initial Slack command payload')
def run(token, team_id, team_domain, channel_id, channel_name, user_id, user_name, command, text, response_url, url ):
    """
    Simulates the Slack client by posting a standard Slack payload to the bot endpoint. The URL of the endpoint as well as all values in the payload can be overriden using command line options. The payload format is documented at https://api.slack.com/slash-commands#triggering_a_command
    """
    data = {'token': token,
            'team_id': team_id,
            'team_domain': team_domain,
            'channel_id': channel_id,
            'channel_name': channel_name,
            'user_id': user_id,
            'user_name': user_name,
            'command': command,
            'text': text,
            'response_url': response_url}

    requests.post(url, data=data)

if __name__ == '__main__':
    run()

