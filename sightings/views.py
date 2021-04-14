from django.shortcuts import render
from .models import Sight
from django.shortcuts import redirect
from .forms import SightForm


def homepage_view(request):
    return render(request,'sightings/homepage.html')

def list_sights(request):
    sights = Sight.objects.all()
    fields = ['Unique_Squirrel_Id','Date']
    context = {
            'sights':sights,
            'fields':fields,
            }
    return render(request, 'sightings/list.html', context)

def update_sights(request,Unique_Squirrel_Id):
    sight = Sight.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
    if request.method == 'POST':
        form = SightForm(request.POST, instance = sight)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SightForm(instance = sight)

    context = {
            'form':form,
            }
    return render(request, 'sightings/update.html', context)

def add_sights(request):
    if request.method == 'POST':
        form = SightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightForm()

    context = {
            'form':form,
            }

    return render(request, 'sightings/add.html', context)

def stats_view(request):

    sights = Sight.objects.all()

    # shift
    AM_n = sights.filter(Shift='AM').count()
    PM_n = sights.filter(Shift='PM').count()
    AM_pct = "{:.2%}".format(AM_n / sights.count())
    PM_pct = "{:.2%}".format(PM_n / sights.count())
    # age
    Juvenile_n = sights.filter(Age='Juvenile').count()
    Adult_n = sights.filter(Age='Adult').count()
    Juvenile_pct = "{:.2%}".format(Juvenile_n / sights.count())
    Adult_pct = "{:.2%}".format(Adult_n / sights.count())
    # Eating
    Eating_True = sights.filter(Eating='True').count()
    Eating_False = sights.filter(Eating='False').count()
    Eating_True_pct = "{:.2%}".format(Eating_True / sights.count())
    Eating_False_pct = "{:.2%}".format(Eating_False / sights.count())
    # Running
    Running_True = sights.filter(Running='True').count()
    Running_False = sights.filter(Running='False').count()
    Running_True_pct = "{:.2%}".format(Running_True / sights.count())
    Running_False_pct = "{:.2%}".format(Running_False / sights.count())
    # Climbing
    Climbing_True = sights.filter(Climbing='True').count()
    Climbing_False = sights.filter(Climbing='False').count()
    Climbing_True_pct = "{:.2%}".format(Climbing_True / sights.count())
    Climbing_False_pct = "{:.2%}".format(Climbing_False / sights.count())

    context = {
            'Shift': {'AM': AM_n,'PM': PM_n},
            'Shift_pct': {'AM': AM_pct,'PM': PM_pct},
            'Age': {'Juvenile': Juvenile_n, 'Adult': Adult_n},
            'Age_pct': {'Juvenile': Juvenile_pct, 'Adult': Adult_pct},
            'Eating': {'Eating_True':Eating_True, 'Eating_False':Eating_False},
            'Eating_pct': {'Eating_True':Eating_True_pct, 'Eating_False':Eating_False_pct},
            'Running': {'Running_True':Running_True, 'Running_False':Running_False},
            'Running_pct': {'Running_True':Running_True_pct, 'Running_False':Running_False_pct},
            'Climbing': {'Climbing_True':Climbing_True, 'Climbing_False':Climbing_False},
            'Climbing_pct': {'Climbing_True':Climbing_True_pct, 'Climbing_False':Climbing_False_pct},
            }
    return render(request, 'sightings/stats.html', {'context':context})
