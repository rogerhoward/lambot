#!/usr/bin/env python
import os
import requests
from pprint import pprint
import click
import boto3

dynamodb = boto3.client('dynamodb')
finger_message = 'hello, is there anybody in there?'

dynamodb.put_item(TableName='finger', Item={'username': {'S': 'rogerhoward'}, 'message': {'S': finger_message}})

