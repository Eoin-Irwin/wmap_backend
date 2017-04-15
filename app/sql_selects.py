from app.models import DublinBikes

SELECT_ALL_DATA_VALUES = DublinBikes.objects.values('position', 'stand_number', 'stand_name', 'total_bike_stands',
                                                    'available_bike_stands','available_bikes', 'last_update')
