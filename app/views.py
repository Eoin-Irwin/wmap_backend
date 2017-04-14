from django.http import HttpResponse
from django.template.response import TemplateResponse
from app.dublin_bikes_api import json_data_import
from .sql_selects import SELECT_ALL_LOCATIONS, SELECT_NAME


def view_json_data(request):
    json_data = json_data_import()
    return HttpResponse(json_data)


def landing(request):
    all_locations = SELECT_ALL_LOCATIONS
    stand_name = SELECT_NAME
    return TemplateResponse(request, 'app/index.html', {"data": all_locations, 'stands': stand_name})
