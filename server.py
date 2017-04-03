#!/usr/bin/env python
import os
import flask
import boto3
import config
import plugins

from pprint import pprint

app = flask.Flask(__name__)


#------------------------------------------------#
#  Bot endpoint                                  #
#------------------------------------------------#

@app.route('/', methods=['POST'])
def bot():
    """
    Main route which handles inbound Slack commands.
    """

    # Grab form data from Slack inbound, and pass it to plugin dispatch
    # Payload format documented at https://api.slack.com/slash-commands#how_do_commands_work
    command_data = flask.request.form.to_dict()

    # Load plugin.info for each plugin into a list, to make available to context
    plugins_list = [plugins.plugin_source.load_plugin(x).Action(command_data, {}).info for x in plugins.plugin_names]

    # Generate context object, populating it with state we might want to access from within a plugin
    # Making this explicit to force discussions about including new data in context
    context_data = {'plugins': plugins_list, 'active': True}
    for plugin_name in plugins.plugin_names:
        # Send payload dict to each plugin synchronously
        # Should make this async so plugins execute in parallel
        # to avoid one plugin blocking others
        plugins.plugin_source.load_plugin(plugin_name).Action(command_data, context_data)

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
    plugins_list = [plugins.plugin_source.load_plugin(x).Action(None, None).info for x in plugins.plugin_names]

    return flask.jsonify({'env': config.ENV, 'plugins': plugins_list})


#------------------------------------------------#
#  Command line options                          #
#------------------------------------------------#

def run():
    app.run(processes=3, host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    run()
