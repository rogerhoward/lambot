#!/usr/bin/env python
import os, sys


# Root directory of the project
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to a writeable filesystem. Shouldn't need to change this.
TEMP_DIR = '/tmp/'

# Path to the directory for static files
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')


# Meetup API key
MEETUP_KEY = '17a7d2079507022374365d23417e'

#------------------------------------------------#
# ENV VARS                                       #
#------------------------------------------------#

ENV = dict(os.environ)


# Used for templates and other places where we need to prepend the
# name of the Zappa stage to the URL when deployed, but not 
# during local testing
if ENV.get('STAGE'):
    URL_PREFIX = '/{}'.format(ENV.get('STAGE'))
else:
    URL_PREFIX = ''

# Make sure no AWS security credentials are in ENV
if 'AWS_SECURITY_TOKEN' in ENV:
    del ENV['AWS_SECURITY_TOKEN']
if 'AWS_SECRET_ACCESS_KEY' in ENV:
    del ENV['AWS_SECRET_ACCESS_KEY']


#------------------------------------------------#
# Context dict for passing to templates          #
#------------------------------------------------#

CONTEXT = {'URL_PREFIX': URL_PREFIX, 'ENV': ENV}