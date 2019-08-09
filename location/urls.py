from django.urls import path

from .views import *

app_name = 'location'

urlpatterns = [
    path('', LocationInformation.as_view(), name='location')
]