#!/usr/bin/env python
import os
import flask
import boto3
import config

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

app = flask.Flask(__name__)


#------------------------------------------------#
#  Bot endpoint                                  #
#------------------------------------------------#

@app.route('/', methods=['POST'])
def bot():
    """
    Main route which handles inbound Slack commands.
    """

    command_data = flask.request.form

    if command_data['text'] == '':
        message = 'Hello world!'
    else:
        message = command_data['text']

    response = {'text': message, 'response_type': 'in_channel'}
    return flask.jsonify(response)


#------------------------------------------------#
# Supporting endpoints                           #
#------------------------------------------------#


@app.route('/info/')
def info():
    """
    Route which returns all environment variables as a JSON object.
    """
    return flask.jsonify({'env': config.ENV})


@app.route('/static/<path:filepath>')
def serve_static(filepath):
    """
    Route for serving static assets directly, rather than using S3.
    Used for CSS, JS and other assets needed for the application.
    """
    return flask.send_from_directory(config.STATIC_ROOT, filepath)


#------------------------------------------------#
#  Command line options                          #
#------------------------------------------------#

def run():
    app.run(processes=3, host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    run()
