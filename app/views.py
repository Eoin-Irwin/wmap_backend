import datetime

from django.http import HttpResponse

from app.dublin_bikes_api import json_data_import


def datetime_now(request):
    current = datetime.datetime.now()
    html_view = "<html><body>The time is {}</body> </html>".format(current)
    return HttpResponse(html_view)


def view_json_data(request):
    json_data = json_data_import()
    return HttpResponse(json_data)
