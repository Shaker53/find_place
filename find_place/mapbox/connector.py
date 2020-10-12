# -*- coding: utf-8 -*-

import requests
from urllib import parse
import os
from dotenv import load_dotenv


ROOTDIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


dotenv_path = os.path.join(ROOTDIR, '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def search_in_mapbox(place_name):
    url_pattern = os.getenv("URL_PATTERN")
    mapbox_token = os.getenv("TOKEN")
    place_name_encoded = parse.quote(place_name)
    url = url_pattern.format(place_name_encoded, mapbox_token)

    return requests.get(url).json()
