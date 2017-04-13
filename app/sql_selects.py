from app.models import DublinBikes

SELECT_ALL_INFO = DublinBikes.objects.all()

SELECT_ALL_LOCATIONS = DublinBikes.objects.values('position')

