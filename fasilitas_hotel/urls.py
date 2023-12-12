from django.urls import path
from fasilitas_hotel.views import fasilitashotel_view, fasilitashotel_nodata_view, form_add_fasilitas_view, fasilitashotel_delete, fasilitashotel_modify

app_name = "fasilitas_hotel" 

urlpatterns = [
    path('', fasilitashotel_view, name='fasilitashotel'),
    path('fasilitashotel_nodata/', fasilitashotel_nodata_view, name='fasilitashotel_nodata'),
    path('add_fasilitas/', form_add_fasilitas_view, name='form_add_fasilitas'),
    path('delete/', fasilitashotel_delete, name='fasilitashotel_delete'),
    path('modify', fasilitashotel_modify, name='fasilitashotel_modify'),
]