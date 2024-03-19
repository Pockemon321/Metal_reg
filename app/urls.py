from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('delete_product/<int:product_id>/',
         delete_product, name='delete_product'),
    path('update_product/<int:product_id>/',
         update_product, name='update_product'),
    path('delivery/', delivery, name='delivery'),
    path('about/', about, name='about'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', login, name='login')
]
