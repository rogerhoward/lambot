import requests
import json
import datetime
import arrow
from action import SimpleAction
import config
import boto3
from pprint import pprint

class Action(SimpleAction):
    name = 'finger'
    title = 'A simple finger-like service.'
    description = 'Provies a simple service like the old unix finger command. Users can maintain a finger file - like a social media profile - and that others can read.'
    version = 0.1
    help_command = 'finger help'
    help_string = '"/lambot finger $username" will show the finger file for the user whose name was provided.\n"/lambot finger update: $message" will update your finger file with the provided message.\n"/lambot finger listall" will list all users with finger files.'

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
            self.dynamodb.put_item(TableName=self.name, Item={'username': {'S': self.user_name}, 'message': {'S': finger_message}})
            response_payload = {'text': 'your finger file has been updated', 'response_type': self.response_type}
        
        elif self.text == ('finger listall'):
            usernames = []
            response = self.dynamodb.scan(TableName=self.name, AttributesToGet=['username'])
            data = response['Items']

            while 'LastEvaluatedKey' in response:
                response = self.dynamodb.scan(TableName=self.name, AttributesToGet=['username'], ExclusiveStartKey=response['LastEvaluatedKey'])
                data.extend(response['Items'])

            for item in data:
                usernames.append(item['username']['S'])

            message = 'users with finger files: {}'.format(', '.join(usernames)) 
            response_payload = {'text': message, 'response_type': self.response_type}

        else:
            username = self.text[7:]
            rec = self.dynamodb.get_item(TableName=self.name, Key={'username':{'S': username}})

            if 'Item' in rec:
                user_finger_file = rec['Item']['message']['S']
                message = '{} says: {}'.format(username, user_finger_file)
                response_payload = {'text': message, 'response_type': self.response_type}
            else:
                response_payload = {'text': 'that username is not recognized', 'response_type': self.response_type}

        return response_payload