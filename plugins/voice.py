# import requests
# import json


# class Action(object):
#     channels = ['bot', ]
#     payload = None
#     response_type = 'ephemeral'

#     def __init__(self, payload):
#         print('loading voice with', payload)
#         self.payload = payload

#         if self.channels and self.payload['channel'] in self.channels:
#             try:
#                 self.respond()
#             except:
#                 print('plugin {} failed. WTF.'.format(self.info['name']))

#     @property
#     def info(self):
#         return {'name': 'voice', 
#                 'title': 'Voice Synth', 
#                 'description': 'A text-to-speech synthesizer.', 
#                 'version': 1.0}

#     def respond(self):
#         pass

