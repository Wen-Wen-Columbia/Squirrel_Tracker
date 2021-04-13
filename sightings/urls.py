from django.urls import path

from . import views

urlpatterns = [
	    path('',views.homepage_view),
	    path('sightings/',views.list_sights),
	    path('sightings/<Unique_Squirrel_Id>/',views.update_sights),
	    path('add/',views.add_sights),
	    path('stats/',views.stats_view),
	    ]
