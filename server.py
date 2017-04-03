#!/usr/bin/env python
import os
import flask
import boto3
from pluginbase import PluginBase
import config
from pprint import pprint

from plugins.calendar import Action

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

app = flask.Flask(__name__)


plugin_source = PluginBase(package='plugins').make_plugin_source(searchpath=['./plugins'])
plugin_names = plugin_source.list_plugins()


#------------------------------------------------#
#  Bot endpoint                                  #
#------------------------------------------------#

@app.route('/', methods=['POST'])
def bot():
    """
    Main route which handles inbound Slack commands.
    """

    # Grab form data from Slack inbound, and pass it to plugin dispatch
    command_data = flask.request.form.to_dict()
    print(command_data)

    # Payload format documented at https://api.slack.com/slash-commands#how_do_commands_work
    print(command_data)
    for plugin_name in plugin_names:
        # Send payload dict to each plugin synchronously
        # Should make this async so plugins execute in parallel
        # to avoid one plugin blocking others
        plugin_source.load_plugin(plugin_name).Action(command_data)

    # Respond with a HTTP 200
    # In some cases, a bot might want to send an actual payload back with 
    # the immediate response, but for this project all responses come from
    # plugins which use a Webhook to send the response instead.
    response = flask.Response()
    response.status_code = 200
    return response



@app.route('/test/response', methods=['POST'])
def test_response():
    """
    Main route which handles inbound Slack commands.
    """

    # Grab form data from Slack inbound, and pass it to plugin dispatch
    if flask.request.is_json:
        pprint(flask.request.get_json())

    response = flask.Response()
    response.status_code = 200
    return response

    



#------------------------------------------------#
# Supporting endpoints                           #
#------------------------------------------------#

@app.route('/info/')
def info():
    """
    Route which returns environmental info as a JSON object.
    """
    plugins_list = [plugin_source.load_plugin(x).Action(None).info for x in plugin_names]

    return flask.jsonify({'env': config.ENV, 'plugins': plugins_list})


#------------------------------------------------#
#  Command line options                          #
#------------------------------------------------#

def run():
    app.run(processes=3, host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    run()
