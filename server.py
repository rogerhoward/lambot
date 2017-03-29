#!/usr/bin/env python
import os
import flask
import boto3
from pluginbase import PluginBase
import config

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

app = flask.Flask(__name__)


plugin_source = PluginBase(package='plugins').make_plugin_source(searchpath=['./plugins'])
plugin_names = plugin_source.list_plugins()
plugins = [plugin_source.load_plugin(x).Action() for x in plugin_names]

#------------------------------------------------#
#  Bot endpoint                                  #
#------------------------------------------------#

@app.route('/', methods=['POST'])
def bot():
    """
    Main route which handles inbound Slack commands.
    """

    command_data = flask.request.form

    for plugin in plugins:
        if plugin.load(command_data):
            response = {'text': plugin.response, 'response_type': 'in_channel'}
            return flask.jsonify(response)


#------------------------------------------------#
# Supporting endpoints                           #
#------------------------------------------------#


@app.route('/info/')
def info():
    """
    Route which returns environmental info as a JSON object.
    """
    plugins_list = [x.info for x in plugins]
    return flask.jsonify({'env': config.ENV, 'plugins': plugins_list})


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
