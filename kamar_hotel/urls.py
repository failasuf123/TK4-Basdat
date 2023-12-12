from django.urls import path
from .views import kamarhotel_view,form_add_fasilitas_kamar_view,form_add_kamar_view,delete

app_name = "kamar_hotel" 

urlpatterns = [
    path('', kamarhotel_view, name='kamarhotel'),
    path('add_fasilitas/<str:id>/', form_add_fasilitas_kamar_view, name='form_add_fasilitas_kamar'),
    path('add_kamar/', form_add_kamar_view, name='form_add_kamar'),
    path('delete/<str:id>', delete, name='delete'),
]
