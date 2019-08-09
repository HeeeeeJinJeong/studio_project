from django.urls import path

from .views import *

app_name = 'costume'

urlpatterns = [
    path('', CostumeProductList.as_view(), name='list'),
    path('detail/<int:pk>/', CostumeProductDetail.as_view(), name='detail'),
    path('<slug>/', CostumeProductList.as_view(), name='product_in_category'),
]