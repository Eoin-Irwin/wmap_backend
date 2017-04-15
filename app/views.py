from django.http import HttpResponse
from django.template.response import TemplateResponse
from app.dublin_bikes_api import json_data_import
from .sql_selects import SELECT_ALL_DATA_VALUES


def view_json_data(request):
    json_data = json_data_import()
    return HttpResponse(json_data)


def index(request):
    return TemplateResponse(request, 'app/index.html')


def landing(request):
    all_data = SELECT_ALL_DATA_VALUES
    return TemplateResponse(request, 'app/all_bike_stations.html', {"data": all_data})
