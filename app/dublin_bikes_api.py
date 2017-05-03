# noinspection PyCompatibility
import datetime

import requests
from django.contrib.gis.geos import Point
from django.utils import timezone


# Get request on api (api key was requested for real time data)
def json_data_import():
    r = requests.get(
        'https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=a6c1b6c4bac2222a2b80e49abf91bbfddd45e5e2')
    # Make data go from str to json
    dub_json_data = r.json()
    # Position will be made into the point field
    for i in dub_json_data:
        i['last_update'] = datetime.datetime.now()
        i['position'] = Point(float(i['position']['lng']), float(i['position']['lat']))
    return dub_json_data


json_data_import()
