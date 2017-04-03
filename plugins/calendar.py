import requests
import json
import datetime
import arrow
from action import SimpleAction
import config

class Action(SimpleAction):
    name = 'calendar'
    title = 'Calendar of Events'
    description = 'Calendar of Events'
    version = 0.1

    feed = 'https://www.meetup.com/code-and-coffee-long-beach/events/atom/'

    def in_channel(self):
        return True

    def check(self):
        if self.text.startswith('calendar'):
            print('calendar active and responding...')
            return True
        else:
            print('calendar not responding...')
            return False


    def response(self):

        url = 'https://api.meetup.com/2/events'
        data = {'offset': 0, 'page': 20, 'format': 'json', 'limited_events': 'False', 'group_urlname': 'code-and-coffee-long-beach', 'photo-host': 'public', 'status':'upcoming', 'key': config.MEETUP_KEY, 'order': 'time', 'desc': 'false', 'fields': ''}

        r = requests.get(url, params=data)

        if r.status_code != requests.codes.ok:
            return None

        meetups = r.json().get('results', [])

        if len(meetups) > 0:
            next_meet = meetups[0]
            venue = next_meet['venue']

            # Convert milliseconds-since-epoch into Python Arrow (datetime-ish) object
            event_time_local = arrow.get(datetime.datetime.fromtimestamp(next_meet['time']/1000), 'US/Pacific')
            
            # Add time to venue dict, for use in string formatting
            venue['timedate'] = event_time_local.humanize()

            # Create a nice summary message for this event
            message = 'The next Meetup will be {timedate} at {name}, located at {address_1}, {city}, {state}'.format(**venue)

            # Get Google Map static image
            location_escaped = '{address},+{city},+{state}'.format(**{'address': venue['address_1'].replace(' ', '+'), 'city': venue['city'].replace(' ', '+'), 'state': venue['state'].replace(' ', '+')})
            map_image = 'https://maps.googleapis.com/maps/api/staticmap?center={location}&zoom=15&scale=2&size=400x400&maptype=roadmap&format=png&visual_refresh=true&markers=size:mid%7Ccolor:0xff0000%7Clabel:1%7C{location}'.format(**{'location': location_escaped})

            # Create Slack attachment to return
            attachment = {'title': '{} event location'.format(event_time_local.format('MMMM DD, YYYY')), 'title_link': next_meet.get('event_url'), 'image_url': map_image}

            # Create Slack response payload
            response_payload = {'text': message, 'response_type': self.response_type, 'attachments': [attachment]}
            return response_payload

        else:
            return None
