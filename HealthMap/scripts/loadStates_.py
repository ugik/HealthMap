from xml.dom import minidom
from HealthMap.models import Region, Polyline

def run():
    print "Reading State data"
    xmldoc = minidom.parse('HealthMap/scripts/states.xml')
    cNodes = xmldoc.childNodes
    sList = cNodes[0].getElementsByTagName("state")     # top level in DOM is States

    for state in sList: # iterate through each State
        # create the State record in Region table
        print ("%s (%s)" % (state.getAttribute('name'), state.getAttribute('abbrev')))
            
        pList = state.getElementsByTagName("point")
        
        print ("... %s lat/lng points" % len(pList))
