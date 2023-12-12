
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kamarhotel/', include('kamar_hotel.urls')),
    path('fasilitashotel/', include('fasilitas_hotel.urls')),
    path('', include('main.urls'))
]
