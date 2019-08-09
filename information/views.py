from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView

from .models import *


class Information(ListView):
    model = Information
    template_name = 'information/information_list.html'