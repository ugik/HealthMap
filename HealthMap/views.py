from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.db import models
from django.http import HttpResponse
from HealthMap.models import Dataset, Datarow, Region, Polyline, Range, History
from HealthMap.forms import LookupForm
import json, simplejson
import urllib, urllib2
import sys

def HomePage(request):
    empty_dataset = Dataset.objects.get(name='Empty') 
    dataset_id = request.GET.get('id')    # Dataset passed as URL param
    dataset = empty_dataset     # use empty dataset as default

    if dataset_id!=None:
        data = Dataset.objects.filter(id=dataset_id)
        if data:
            dataset = data[0]

    dataset_range = datasetRange(dataset)   # figure out what our ranges are (explicit or implicit)
            
    form = LookupForm()
    context = ({'form': form, 'dataset': dataset, 'dataset_range': dataset_range})
    return render_to_response('index.html', context, context_instance=RequestContext(request))


def LookupRequest(request):
    form = LookupForm(request.POST)
    if form.is_valid():
        data = Dataset.objects.filter(name=form.cleaned_data['autocomplete'])
        print("Latitude: %s" % form.cleaned_data['latitude'])
        print("Longitude: %s" % form.cleaned_data['longitude'])
        if data:
            dataset_chosen = data[0].id
            if data[0].name != 'Empty':     # track history of non-Empty maps rendered
                history = History(name=data[0].name, 
                                          latitude=form.cleaned_data['latitude'][0:15],
                                          longitude=form.cleaned_data['longitude'][0:15])
                history.save()

            return redirect('/?id=%s' % dataset_chosen)
        else:
            return redirect('/')
    else:
        print "Form is not valid"

    context = ({'form': form})
    return render_to_response('index.html', context, context_instance=RequestContext(request))

def RandomRequest(request):
    data = Dataset.objects.order_by('?')[0]
    if data:
        dataset_chosen = data.id
        return redirect('/?id=%s' % dataset_chosen)
    else:
        return redirect('/')

    context = ({})
    return render_to_response('index.html', context, context_instance=RequestContext(request))


# provides gis data for dataset to render map polygons
def dataset_gis(request):
    try:
        dataset_id = request.GET.get('id', '')
        dataset = Dataset.objects.get(id=int(dataset_id))
        dataset_range = datasetRange(dataset)

        results = []

#        import pdb; pdb.set_trace()
        
        for row in dataset.datarow_set.all():
            data = {}
            data['state'] = row.region.state
            data['county'] = row.region.county
            data['value'] = str(row.value)
            if row.color()=="#FFFFF0":
                for ran in dataset_range:
#                    print("[%s] low:%s high:%s" % (row.value, ran.low, ran.high))
#                    print("row value:%s  low/high:%s" % (row.value.__class__, ran.low.__class__))
                    if row.value >= ran.low and row.value <= ran.high:
                        data['color'] = ran.color
            else:
                data['color'] = row.color()
            
            points = []
            for line in row.region.polyline_set.order_by('pk'):
                pts = {}
                pts['lat'] = str(line.lat)
                pts['lng'] = str(line.lng)
                points.append(pts)

            data['points'] = points    # points array within the data array
            results.append(data)

#        print ("dataset:%s  gis elements:%s" % (dataset.name, len(results)))

        return_data = json.dumps(results)
        return HttpResponse(return_data, mimetype='application/javascript')
    except Exception, e:
        print e

# show map history    
def showHistory(request):

    def get_geonames(lat, lng, types):
        try:
            url = 'http://maps.googleapis.com/maps/api/geocode/json' + \
                    '?latlng={},{}&sensor=false'.format(lat, lng)
            jsondata = json.load(urllib2.urlopen(url))
            address_comps = jsondata['results'][0]['address_components']
            filter_method = lambda x: len(set(x['types']).intersection(types))
            return filter(filter_method, address_comps)
        except Exception, e:
            print e
            return filter(None, None)
            
    class history_mimic(object):
        def __init__(self, id=None, name=None, searched=None, latitude=None, longitude=None, location=None):
            self.id = id
            self.name = name
            self.searched = searched
            self.latitude = latitude
            self.longitude = longitude
            self.location = location
 
    recent_maps = []
    history = History.objects.order_by('-searched')[:30]
    for h in history:
        dataset = Dataset.objects.filter(name__icontains=h.name)
        if dataset:
            location = ""
            if h.latitude!=None and len(h.latitude)>1:      # reverse geolocation
                types = ['locality', 'administrative_area_level_1', 'country']
                try:
                    for geoname in get_geonames(h.latitude, h.longitude, types):
        #                common_types = set(geoname['types']).intersection(set(types))
                        if geoname['long_name']!='United States':   # show only non-US country
                            location = location+geoname['long_name'] + " "
                except Exception, e:
                    print e

            recent_maps.append(history_mimic(id=dataset[0].id, 
                                                                    name=h.name, 
                                                                    searched=h.searched.strftime("%m/%d %H:%M"),
                                                                    latitude = h.latitude,
                                                                    longitude = h.longitude,
                                                                    location = location))
        
    context = ({'history': recent_maps})
    return render_to_response('history.html', context, context_instance=RequestContext(request))


# used by JQuery autocomplete widget
def dataset_lookup(request):
    try:
        if request.is_ajax():
            q = request.GET.get('term', '')
            data = Dataset.objects.filter(name__icontains = q )[:20]
 #           print("q:%s rows:%s" % (q, len(data)))
            results = []
            for d in data:
                data_json = {}
                data_json['id'] = d.id
                data_json['label'] = d.name
                data_json['value'] = d.name
                results.append(data_json)
            return_data = json.dumps(results)
#            print("Results: %s" % len(results))
        else:
            return_data = 'fail'
        mimetype = 'application/json'
        return HttpResponse(return_data, mimetype)
    except Exception, e:
        print e

# figure out a range to use for legend
def datasetRange(dataset):
    dataset_range = Range.objects.filter(dataset=dataset)
    empty_dataset = Dataset.objects.get(name='Empty') 

    if not dataset_range:       # establish a default range from the Empty dataset
        # create a list of objects to mimic a dataset range using default range from Empty dataset
        class range_mimic(object):
            def __init__(self, name=None, low=None, high=None, color=None):
                self.name = name
                self.low = low
                self.high = high
                self.color = color

        row = dataset.datarow_set.all().order_by('value')
        dataset_range = []
        default_range = Range.objects.filter(dataset=empty_dataset)
        range_name = ['Low', 'Low-Mid', 'Mid', 'Mid-High', 'High', 'Very High']
        range_elements = 6
        for i in range(range_elements):      # assume legend of 6 elements
            if i==range_elements-1:
                dataset_range.append(range_mimic(name=range_name[i],
                                                                          low=row[row.count()/6*i].value, 
                                                                          high=row[row.count()-1].value,
                                                                          color=default_range[i].color))
            else:
                dataset_range.append(range_mimic(name=range_name[i], 
                                                                           low=row[row.count()/6*i].value,
                                                                           high=row[row.count()/6*(i+1)].value,
                                                                           color=default_range[i].color))
    return dataset_range












