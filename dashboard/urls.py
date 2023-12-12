from django.urls import path
from dashboard.views import show_dashboard_customer
from dashboard.views import show_dashboard_hotel

app_name = 'dashboard'

urlpatterns = [
    path('customer/', show_dashboard_customer, name='show_dashboard_customer'),
    path('hotel/', show_dashboard_hotel, name="show_dashboard_hotel"),
]