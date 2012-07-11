from django.shortcuts import render_to_response
from django.template import RequestContext
from HealthMap.models import Dataset, Datarow, Region, Polyline

def HomePage(request):
    dataset = Dataset.objects.get(name='Empty')   # use empty dataset by default
    name = request.GET.get('Data')    # Dataset passed as URL param

    if name!=None:
        data = Dataset.objects.filter(name=name)
        if not data:
            dataset = Dataset.objects.get(name='Empty')
        else:
            dataset = data[0]

#    print("Dataset:%s" % dataset.name)
                
    context = {'dataset': dataset}
    return render_to_response('index.html', context, context_instance=RequestContext(request))
    
