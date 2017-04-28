import json
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.template.response import TemplateResponse
from app.distance_of_points import distance_checker
from app.dublin_bikes_api import json_data_import
from app.models import DublinBikes
from .sql_selects import SELECT_ALL_DATA_VALUES
import re

def json_all_stations(request):
    lat = request.GET['lat']
    long = request.GET['long']

    json_data = json_data_import()
    for i in json_data:
        DublinBikes.objects.filter(stand_number=i['number']).update(
            available_bike_stands=i['available_bike_stands'], available_bikes=i['available_bikes'],
            last_update=i['last_update'])
    all_data = SELECT_ALL_DATA_VALUES
    results = {}
    # for every queryset in the list serialize it.
    data = serializers.serialize("json", all_data)
    results[0] = json.loads(data)
    regex = r'\(([^)]+)\)'

    for i in results[0]:
        coords = i['fields']['position']
        res = re.findall(regex,coords)
        blong,blat  =res[0].split(' ')
        dist = distance_checker(lat,long,blat,blong)
        i['distance'] = dist
    return JsonResponse(results)  # return it


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


# def nearby(json_data):
#     # get posted data
#     submitted = json_data
#     # do whatever is necessary to create document
#     data = submitted
#     check_dis = distance_checker(lat=,long=,check_lat=data[0]['position'].y,check_long=data[0]['position'].x)
#     return TemplateResponse(check_dis, 'app/all_bike_stations.html')
