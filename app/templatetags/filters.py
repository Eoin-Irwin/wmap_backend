from django.template.defaulttags import register

from app.distance_of_points import distance_checker


@register.filter
def getpos(dictionary, key):
    return dictionary[0].key


@register.filter
def find_distance(lat, long, check_lat, check_long):
    return distance_checker(lat, long, check_lat, check_long)
