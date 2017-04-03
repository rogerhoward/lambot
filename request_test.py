#!/usr/bin/env python
import os
import requests
from pprint import pprint
import click

@click.command()
@click.option('--token', default='gIkuvaNzQIHg97ATvDxqgjtO', help='Slack token.')
@click.option('--team_id', default='T0001', help='Slack channel to simulate.')
@click.option('--team_domain', default='example', help='Slack channel to simulate.')
@click.option('--channel_id', default='C2147483705', help='Slack channel to simulate.')
@click.option('--channel_name', default='bot', help='Slack channel to simulate.')
@click.option('--user_id', default='U2147483697', help='Username to simulate.')
@click.option('--user_name', default='rogerhoward', help='Username to simulate.')
@click.option('--command', default='/lambot', help='Username to simulate.')
@click.option('--text', default='calendar', help='Username to simulate.')
@click.option('--response_url', default='http://0.0.0.0:5000/test/response', help='Username to simulate.')
def run(token, team_id, team_domain, channel_id, channel_name, user_id, user_name, command, text, response_url ):
    url = 'http://0.0.0.0:5000/'

    data = {'token': token,
            'team_id': team_id,
            'team_domain': team_domain,
            'channel_id': channel_id,
            'channel_name': channel,
            'user_id': user_id,
            'user_name': user_name,
            'command': command,
            'text': text,
            'response_url': response_url}

    requests.post(url, data=data)

if __name__ == '__main__':
    run()

