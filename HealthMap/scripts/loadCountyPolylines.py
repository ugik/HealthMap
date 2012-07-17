from HealthMap.models import Region, Dataset, Datarow, Category, Range, Polyline
import shapefile

def run():

    # clean up if necessary
    print "Loading County Polyline data"

    sf = shapefile.Reader("HealthMap/scripts/US_Counties/US_county_region")

    shapes = sf.shapes()
    records = sf.records()
    print("Processing %s shapes" % len(shapes))
    for i, s in enumerate(shapes):
        fips = records[i][3:4]
        county = records[i][2:3]
        print("FIPS:%s  County:%s" % (fips, county))
        for p in s.points:
            print("lng:%s lat:%s" % (p[0], p[1]))

    print "__________"        
#            line = Polyline(region=reg, lat=point.getAttribute('lat'), lng=point.getAttribute('lng'))
#            line.save()

    

