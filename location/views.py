from django.shortcuts import render

# Create your views here.
from .models import Location
from django.views.generic.list import ListView

class LocationInformation(ListView):
    model = Location
    template_name = 'location/location_list.html'