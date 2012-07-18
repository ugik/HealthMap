from HealthMap.models import Region, Dataset, Datarow, Category, Range, Polyline
import shapefile

def run():

    # clean up if necessary
    print "Loading County Polyline data"

    sf = shapefile.Reader("HealthMap/scripts/US_Counties/US_county_region")
#    sf = shapefile.Reader("HealthMap/scripts/US_Counties_Highres/County_US_region")

    shapes = sf.shapes()
    records = sf.records()
    print("Processing %s shapes" % len(shapes))
    for i, s in enumerate(shapes):
        fips = records[i][3:4]
        state = records[i][0:1]
        county = records[i][2:3]
#        fips = records[i][0:1]
#        state = records[i][2:3]
#        county = records[i][3:4]
        if state[0]=='Massachusetts':
            print("State: %s  FIPS:%s  County:%s  Pts:%s" % (state[0],fips[0], county[0], len(s.points)))
        reg = Region.objects.filter(fips=fips[0])
        if reg:
            lines = Polyline.objects.filter(region=reg[0])
#            if lines:   # cleanup
#                lines.delete()
#            print("%s points" % len(s.points))
#            for p in s.points:
#                print("lng:%s lat:%s" % (p[0], p[1]))
#                if reg:     # assume County regions as built 
#                    line = Polyline(region=reg[0], lat=p[1], lng=p[0])
#                    line.save()
        else:
            print("No region for FIPS:%s" % fips)
    

