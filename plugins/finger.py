import requests
import json
import datetime
import arrow
from action import SimpleAction
import config
import boto3


class Action(SimpleAction):
    name = 'finger'
    title = 'A simple finger-like service.'
    description = 'Provies a simple service like the old unix finger command. Users can maintain a finger file - like a social media profile - and that others can read.'
    version = 0.1
    help_command = 'finger help'
    help_string = '"/lambot finger $username" will show the finger file for the user whose name was provided.\n"/lambot finger update: $message" will update your finger file with the provided message.'

    channels = '*'

    dynamodb = boto3.client('dynamodb')


    def check(self):
        if self.text.startswith(self.name):
            print('finger active and responding...')
            return True
        else:
            print('finger not responding...')
            return False


    def response(self):
        if self.text.startswith('finger update:'):
            finger_message = self.text[14:]
            self.dynamodb.put_item(TableName=self.name, Item={'username': {'S': username}, 'message': {'S': finger_message}})
            response_payload = {'text': 'your finger file has been updated', 'response_type': self.response_type}
        else:
            username = self.text[7:]
            rec = self.dynamodb.get_item(TableName=self.name, Key={'username':{'S': username}})
            if 'item' in rec:
                user_finger_file = rec['item']['message']['S']
                response_payload = {'text': user_finger_file, 'response_type': self.response_type}
            else:
                response_payload = {'text': 'that username is not recognized', 'response_type': self.response_type}

        return response_payload