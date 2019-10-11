from django.urls import path

from .views import Reservation_Create, Reservation_Delete, Reservation_Detail, Reservation_List, Reservation_Update

app_name = 'reservation'

urlpatterns = [
    path('', Reservation_List.as_view(), name='list'),
    path('detail/<int:pk>/', Reservation_Detail.as_view(), name='detail'),
    path('delete/<int:pk>/', Reservation_Delete.as_view(), name='delete'),
    path('create/', Reservation_Create.as_view(), name='create'),
    path('update/<int:pk>/', Reservation_Update.as_view(), name='update'),
]