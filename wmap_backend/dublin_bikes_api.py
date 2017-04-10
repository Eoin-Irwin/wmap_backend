# noinspection PyCompatibility
import urllib.request
from pprint import pprint


def json_data_import():
    x = urllib.request.urlopen(
        'https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=a6c1b6c4bac2222a2b80e49abf91bbfddd45e5e2')
    return x.read()
