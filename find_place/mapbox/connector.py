# -*- coding: utf-8 -*-

import requests
from urllib import parse
import pickle
import os


ROOTDIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
URL_PATTERN = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json?access_token={}'


def search_in_mapbox(place_name):
    token_path = os.path.join(ROOTDIR, 'mapbox', 'token.pickle')
    with open(token_path, 'rb') as f:
        mapbox_token = pickle.load(f)['token']

    place_name_encoded = parse.quote(place_name)
    url = URL_PATTERN.format(place_name_encoded, mapbox_token)

    return requests.get(url).json()
