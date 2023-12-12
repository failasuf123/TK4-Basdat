from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path('register_hotel/', register_hotel, name='register_hotel'),
    path('register_customer/', register_customer, name='register_customer'),
]