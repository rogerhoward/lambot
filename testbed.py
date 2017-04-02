#!/usr/bin/env python
import os
import requests
from pprint import pprint
import config

url = 'https://api.meetup.com/2/events'
data = {'offset': 0, 'page': 20, 'format': 'json', 'limited_events': 'False', 'group_urlname': 'code-and-coffee-long-beach', 'photo-host': 'public', 'status':'upcoming', 'key': config.MEETUP_KEY, 'order': 'time', 'desc': 'false', 'fields': ''}

meetups = requests.get(url, params=data).json().get('results', [])

if len(meetups) > 0:
    next_meet = meetups[1]
    venue = next_meet['venue']
    message = 'The next Meetup is at {name}, located at {address_1}, {city}, {state}'.format(**venue)

    location_escaped = '{address},+{city},+{state}'.format(**{'address': venue['address_1'].replace(' ', '+'), 'city': venue['city'].replace(' ', '+'), 'state': venue['state'].replace(' ', '+')})
    map_image = 'https://maps.googleapis.com/maps/api/staticmap?center={location}&zoom=15&scale=2&size=400x400&maptype=roadmap&format=png&visual_refresh=true&markers=size:mid%7Ccolor:0xff0000%7Clabel:1%7C{location}'.format(**{'location': location_escaped})

    pprint(next_meet)
    print(message)

    print(map_image)