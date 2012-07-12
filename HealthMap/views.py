from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from HealthMap.models import Dataset, Datarow, Region, Polyline
from HealthMap.forms import LookupForm
import simplejson
import urllib

def HomePage(request):
    dataset = Dataset.objects.get(name='Empty')   # use empty dataset by default
    dataset_id = request.GET.get('id')    # Dataset passed as URL param

    if dataset_id!=None:
        data = Dataset.objects.filter(id=dataset_id)
        if not data:
            dataset = Dataset.objects.get(name='Empty')
        else:
            dataset = data[0]

#    print("Dataset:%s" % dataset.name)
    form = LookupForm()
    context = ({'form': form, 'dataset': dataset, 'Datasets': Dataset.objects.all()})
    return render_to_response('index.html', context, context_instance=RequestContext(request))


def LookupRequest(request):
    form = LookupForm(request.POST)
    if form.is_valid():
        data = Dataset.objects.filter(name=form.cleaned_data['autocomplete'])
        if data:
            dataset_chosen = data[0].id
            return redirect('/?id=%s' % dataset_chosen)
        else:
            return redirect('/')
    else:
        print "Form is not valid"

    context = ({'form': form})
    return render_to_response('index.html', context, context_instance=RequestContext(request))
        

def dataset_lookup(request):
    print "In Dataset lookup"
    dataset = Dataset.objects.all()
    results = []
    for data in dataset:
        dataset_dict = {'id':data.id, 'label':data.name, 'value':data.name}
        results.append(dataset_dict)
    return HttpResponse(simplejson.dumps(results),mimetype='application/json')

