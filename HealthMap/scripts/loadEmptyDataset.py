from xml.dom import minidom
from HealthMap.models import Region, Dataset, Datarow, Category
import random

def run():
    print "Loading empty Dataset"

    # create the empty Category
    cat = Category(name="Empty")
    cat.save()

    # clean up if necessary
    dat = Dataset.objects.filter(name='Empty')
    if not dat:
        # create the empty Dataset
        dat = Dataset(category=cat, name="Empty", description="Empty Dataset", legend="Empty")
        dat.save()
    dat = Dataset.objects.filter(name='Empty')

    # create empty ranges
    range = Range(dataset=dat[0], name="Low", low=0, high=10, color="#FFFAFA")
    range.save()
    range = Range(dataset=dat[0], name="Low-Mid", low=10, high=20, color="#F2F2F2")
    range.save()
    range = Range(dataset=dat[0], name="Mid", low=20, high=30, color="#D0CFCF")
    range.save()
    range = Range(dataset=dat[0], name="Mid-High", low=30, high=40, color="#ADACAC")
    range.save()
    range = Range(dataset=dat[0], name="High", low=40, high=50, color="#8B8989")
    range.save()
    range = Range(dataset=dat[0], name="Very High", low=50, high=60, color="#596C56")
    range.save()
    
    row = Datarow.objects.filter(dataset=dat[0])
    if row:
        row.delete()

    # use states.xml to iterate through States
    xmldoc = minidom.parse('HealthMap/scripts/states.xml')
    cNodes = xmldoc.childNodes
    sList = cNodes[0].getElementsByTagName("state")     # top level in DOM is States

    for state in sList: # iterate through each State
        # create the State record in Datarow table with one zero value
        print ("%s (%s)" % (state.getAttribute('name'), state.getAttribute('abbrev')))
        reg = Region.objects.filter(state=state.getAttribute('abbrev'))
        if len(reg)==1:
            row = Datarow(dataset=dat[0], region=reg[0], value=random.randrange(0,60))
            row.save()
            
    print ("... %s values" % len(sList))
