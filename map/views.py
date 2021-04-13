from django.shortcuts import render
from sightings.models import Sight

def map_view(request):
    sights = Sight.objects.all()[:100]
    context = {
            'sights':sights,
            }
    return render(request, 'map/map.html', context)
