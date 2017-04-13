from django.template.defaulttags import register


@register.filter
def getpos(dictionary, key):
    return dictionary[0].key
