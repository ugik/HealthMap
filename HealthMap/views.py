from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from HealthMap.models import Dataset, Datarow, Region, Polyline
import simplejson

def HomePage(request):
    dataset = Dataset.objects.get(name='Empty')   # use empty dataset by default
    name = request.GET.get('Data')    # Dataset passed as URL param

    if name!=None:
        data = Dataset.objects.filter(name=name)
        if not data:
            dataset = Dataset.objects.get(name='Empty')
        else:
            dataset = data[0]

    print("Dataset:%s" % dataset.name)

    context = ({'dataset': dataset, 'Datasets': Dataset.objects.all()})
    return render_to_response('index.html', context, context_instance=RequestContext(request))
    

def dataset_lookup(request):
    print "In Dataset lookup"
    dataset = Dataset.objects.all()
    results = []
    for data in dataset:
        dataset_dict = {'id':data.id, 'label':data.name, 'value':data.name}
        results.append(dataset_dict)
    return HttpResponse(simplejson.dumps(results),mimetype='application/json')

