import requests
import json
import random


class Action(object):
    payload = None
    response_type = 'ephemeral'

    def __init__(self, payload):
        print('loading mememe plugin with', payload)
        # Payload format documented at https://api.slack.com/slash-commands#how_do_commands_work
        self.payload = payload

        try:
            if self.payload.get('text')[0:6].lower() == 'mememe':
                self.respond()
        except:
            print('plugin {} failed. WTF.'.format(self.info['name']))

    @property
    def info(self):
        return {'name': 'mememe', 
                'title': 'Meme Me!', 
                'description': 'Get a random meme - meme me.', 
                'version': 1.0}

    def respond(self):
        r = requests.get('https://api.imgflip.com/get_memes')
        memes = r.json().get('data', {}).get('memes', [])
        if len(memes) > 0:
            random_meme = random.choice(memes)

            if self.payload.get('text') == 'mememe':
                meme_attachment = {'image_url': random_meme['url'], 'fallback': random_meme['name'], 'title': random_meme['name']}
            else:
                caption = self.payload.get('text')[7:]
                custom_meme = requests.post('https://api.imgflip.com/caption_image', data = {'template_id': random_meme['id'], 'username': 'imgflip_hubot', 'password': 'imgflip_hubot', 'text0': caption}).json()


                meme_attachment = {'image_url': custom_meme['data']['url'], 'fallback': random_meme['name'], 'title': random_meme['name']}




            url = self.payload.get('response_url')

            if url:
                response_payload = {'text': 'Your hot, fresh meme:', 'attachments': [meme_attachment], 'response_type': self.response_type}
                requests.post(url, json=response_payload)