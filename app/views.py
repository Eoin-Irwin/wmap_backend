from django.http import HttpResponse
from django.template.response import TemplateResponse
from app.dublin_bikes_api import json_data_import
from app.models import DublinBikes
from .sql_selects import SELECT_ALL_DATA_VALUES


def view_json_data(request):
    json_data = json_data_import()
    return HttpResponse(json_data)


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
