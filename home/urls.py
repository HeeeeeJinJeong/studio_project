from django.urls import path, re_path
from .views import Home_List

app_name = 'home'

urlpatterns = [
    path('', Home_List.as_view(), name='home'),
]