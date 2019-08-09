from django.urls import path

from .views import SceneryList, SceneryDetail

app_name = 'scenery'

urlpatterns = [
    path('', SceneryList.as_view(), name='list'),
    path('detail/<slug>/', SceneryDetail.as_view(), name='detail'),
    path('<slug>/', SceneryList.as_view(), name='room_view_in_category'),
]