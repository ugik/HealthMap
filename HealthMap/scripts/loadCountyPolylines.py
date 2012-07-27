from HealthMap.models import Region, Dataset, Datarow, Category, Range, Polyline
import shapefile

def run():

    # clean up if necessary
    print "Loading County Polyline data"

#    sf = shapefile.Reader("HealthMap/scripts/US_Counties/US_county_region")
    sf = shapefile.Reader("HealthMap/scripts/US_Counties/HI_county_region")

    shapes = sf.shapes()
    records = sf.records()
    print("Processing %s shapes" % len(shapes))
    for i, s in enumerate(shapes):
        fips = records[i][3:4]
        county = records[i][2:3]
        print("FIPS:%s  County:%s" % (fips[0], county[0]))
        reg = Region.objects.filter(fips=fips[0])
        if reg:
            lines = Polyline.objects.filter(region=reg[0])
            if lines:   # cleanup
                lines.delete()
            for p in s.points:
                print("lng:%s lat:%s" % (p[0], p[1]))
                if reg:     # assume County regions as built 
                    line = Polyline(region=reg[0], lat=p[1], lng=p[0])
                    line.save()
        else:
            print("No region for FIPS:%s" % fips)
    

