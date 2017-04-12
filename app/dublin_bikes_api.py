# noinspection PyCompatibility
import requests
import datetime


def json_data_import():
    r = requests.get(
        'https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=a6c1b6c4bac2222a2b80e49abf91bbfddd45e5e2')
    dub_json_data = r.json()

    return dub_json_data


json_data_import()
