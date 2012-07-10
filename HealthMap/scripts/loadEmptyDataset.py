from xml.dom import minidom
from HealthMap.models import Region, Dataset, Datarow, Category

def run():
    print "Loading empty Dataset"

    # create the empty Category
    cat = Category(name="Empty")
    cat.save()
    
    # create the empty Dataset
    dat = Dataset(category=cat, name="Empty", description="Empty Dataset", legend="Empty")
    dat.save()
    
    # use states.xml to iterate through States
    xmldoc = minidom.parse('HealthMap/scripts/states.xml')
    cNodes = xmldoc.childNodes
    sList = cNodes[0].getElementsByTagName("state")     # top level in DOM is States

    for state in sList: # iterate through each State
        # create the State record in Datarow table with one zero value
        print ("%s (%s)" % (state.getAttribute('name'), state.getAttribute('abbrev')))
        reg = Region.objects.filter(state=state.getAttribute('abbrev'))
        if len(reg)==1:
            row = Datarow(dataset=dat, region=reg[0], value=0)
            row.save()
            
    print ("... %s values" % len(sList))
