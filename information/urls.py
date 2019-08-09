from django.urls import path, re_path
from .views import Information

app_name = 'information'

urlpatterns = [
    path('', Information.as_view(), name='information'),
]