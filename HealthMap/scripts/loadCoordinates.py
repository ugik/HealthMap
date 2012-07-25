from HealthMap.models import Dataset

def set_Coordinates(region_name, latitude, longitude, zoom):
    dat = Dataset.objects.filter(name__icontains=": "+region_name)
    for d in dat:
        d.maplatitude = latitude
        d.maplongitude = longitude
        d.mapzoom = zoom
        d.save()
    print("Coordinates set for %s" % region_name)
 
def run():

    region_name = "Pacific Coast"
    region_latitude = "40.5472"
    region_longitude = "-114.499512"
    region_zoom = "5"
    set_Coordinates(region_name, region_latitude, region_longitude, region_zoom)

    region_name = "Mountain"
    region_latitude = "42.065607"
    region_longitude = "-111.027832"
    region_zoom = "5"
    set_Coordinates(region_name, region_latitude, region_longitude, region_zoom)

    region_name = "Southwest"
    region_latitude = "31"
    region_longitude = "-105"
    region_zoom = "5"
    set_Coordinates(region_name, region_latitude, region_longitude, region_zoom)

    region_name = "Heartland"
    region_latitude = "41.5"
    region_longitude = "-96.328125"
    region_zoom = "5"
    set_Coordinates(region_name, region_latitude, region_longitude, region_zoom)

    region_name = "Southeast"
    region_latitude = "31.1"
    region_longitude = "-86.220703"
    region_zoom = "6"
    set_Coordinates(region_name, region_latitude, region_longitude, region_zoom)

    region_name = "Appalachian Highlands"
    region_latitude = "36.597889"
    region_longitude = "-83.166504"
    region_zoom = "6"
    set_Coordinates(region_name, region_latitude, region_longitude, region_zoom)

    region_name = "Midwest"
    region_latitude = "41.72"
    region_longitude = "-85.341797"
    region_zoom = "5"
    set_Coordinates(region_name, region_latitude, region_longitude, region_zoom)

    region_name = "Mid-Atlantic"
    region_latitude = "41"
    region_longitude = "-75.476074"
    region_zoom = "6"
    set_Coordinates(region_name, region_latitude, region_longitude, region_zoom)

    region_name = "New England"
    region_latitude = "43"
    region_longitude = "-70.861816"
    region_zoom = "6"
    set_Coordinates(region_name, region_latitude, region_longitude, region_zoom)

    region_name = "Alaska"
    region_latitude = "64.396938"
    region_longitude = "-150"
    region_zoom = "4"
    set_Coordinates(region_name, region_latitude, region_longitude, region_zoom)

    region_name = "Hawaii"
    region_latitude = "20.653346"
    region_longitude = "-157.412109"
    region_zoom = "7"
    set_Coordinates(region_name, region_latitude, region_longitude, region_zoom)



