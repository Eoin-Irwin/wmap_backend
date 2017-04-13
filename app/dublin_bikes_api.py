# noinspection PyCompatibility
import requests
from time import gmtime, strftime


def json_data_import():
    r = requests.get(
        'https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=a6c1b6c4bac2222a2b80e49abf91bbfddd45e5e2')
    dub_json_data = r.json()
    for i in dub_json_data:
        i['last_update'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        i['longitude'] = i['position']['lng']
        i['latitude'] = i['position']['lat']

    return dub_json_data


json_data_import()
