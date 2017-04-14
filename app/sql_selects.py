from app.models import DublinBikes

SELECT_ALL_INFO = DublinBikes.objects.all()

SELECT_ALL_LOCATIONS = DublinBikes.objects.values('position')

SELECT_NAME = DublinBikes.objects.values('stand_name')