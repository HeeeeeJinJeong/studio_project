from django.conf.urls import url
from django.urls import path
from . import views
from .views import EventDetail, EventList

app_name = 'schedule'

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    path('detail/<int:pk>/', EventDetail.as_view(), name='detail'),
    path('list/', EventList.as_view(), name='list'),
]