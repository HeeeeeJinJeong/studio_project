from django.urls import path

from .views import Appointment_Create, Appointment_Delete, Appointment_Detail, Appointment_List, Appointment_Update

app_name = 'appointment'

urlpatterns = [
    path('', Appointment_List.as_view(), name='list'),
    path('detail/<int:pk>/', Appointment_Detail.as_view(), name='detail'),
    path('delete/<int:pk>/', Appointment_Delete.as_view(), name='delete'),
    path('create/', Appointment_Create.as_view(), name='create'),
    path('update/<int:pk>/', Appointment_Update.as_view(), name='update'),
]