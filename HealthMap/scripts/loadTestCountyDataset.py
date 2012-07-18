from xml.dom import minidom
from HealthMap.models import Region, Dataset, Datarow, Category, Range
import random

def run():

    print "Loading test County Dataset"

    # clean up if necessary
    cat = Category.objects.filter(name='Test')
    if not cat:
        # create the test Category
        cat = Category(name="Test")
        cat.save()
        print "Created Category"
    cat = Category.objects.filter(name='Test')

    # clean up if necessary
    dat = Dataset.objects.filter(name='TestCounties')
    if dat:
        dat.delete()
        print "Deleted Dataset"
    
    # create a test Dataset
    dat = Dataset(category=cat[0], name="TestCounties", description="Counties Test Dataset", legend="Empty")
    dat.save()
    print "Created Test County Dataset"

    reg = Region.objects.filter(state='MA')
    # populate datasets
    for r in reg:
        if r.fips != None and len(r.fips) == 5:
            row = Datarow(dataset=dat, region=r, value=random.randrange(0,100))
            row.save()

    print("%s County rows created" % len(reg))
                

