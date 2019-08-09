from django.shortcuts import render

# Create your views here.
from .models import Home

from django.views.generic.list import ListView

class Home_List(ListView):
    model = Home
    template_name = 'home/home_list.html'