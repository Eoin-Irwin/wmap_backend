import json, re
import requests
from django.core import serializers
from django.http import JsonResponse
from django.template.response import TemplateResponse
from app.distance_of_points import distance_checker
from app.dublin_bikes_api import json_data_import
from app.models import DublinBikes
from .sql_selects import SELECT_ALL_DATA_VALUES


def json_all_stations(request):
    lat = request.GET['lat']
    long = request.GET['long']

    json_data = json_data_import()
    for i in json_data:
        DublinBikes.objects.all()
    all_data = SELECT_ALL_DATA_VALUES
    results = {}
    # for every queryset in the list serialize it.
    data = serializers.serialize("json", all_data)
    results[0] = json.loads(data)
    regex = r'\(([^)]+)\)'

    for i in results[0]:
        coords = i['fields']['position']
        res = re.findall(regex, coords)
        blong, blat = res[0].split(' ')
        dist = distance_checker(lat, long, blat, blong)
        dist = float(dist) / 1000
        dist = round(dist, 2)
        i['distance'] = dist
    return JsonResponse(results)


def index(request):
    return TemplateResponse(request, 'app/index.html')


def all_stations(request):
    json_data = json_data_import()
    for i in json_data:
        DublinBikes.objects.filter(stand_number=i['number']).update(
            available_bike_stands=i['available_bike_stands'], available_bikes=i['available_bikes'],
            last_update=i['last_update'])
    all_data = SELECT_ALL_DATA_VALUES
    return TemplateResponse(request, 'app/all_bike_stations.html', {"data": all_data})


def find_nearset_station(request):
    address = request.GET.get('address')
    google_url = "https://maps.googleapis.com/maps/api/geocode/json?address={0}".format(address)
    google_reply = requests.get(google_url)
    location_data = json.loads(google_reply.text)
    lat = location_data['results'][0]['geometry']['location']['lat']
    lng = location_data['results'][0]['geometry']['location']['lng']

    json_data = json_data_import()
    for i in json_data:
        DublinBikes.objects.all()
    all_data = SELECT_ALL_DATA_VALUES
    results = {}
    # for every queryset in the list serialize it.
    data = serializers.serialize("json", all_data)
    results[0] = json.loads(data)
    regex = r'\(([^)]+)\)'

    for i in results[0]:
        coords = i['fields']['position']
        res = re.findall(regex, coords)
        blong, blat = res[0].split(' ')
        dist = distance_checker(lat, lng, blat, blong)
        dist = float(dist) / 1000
        dist = round(dist, 2)
        i['distance'] = dist
    return TemplateResponse(request, 'app/find_nearset_station.html', results)
