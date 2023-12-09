from django.shortcuts import render

def kamarhotel_view(request):
    return render(request, 'kamarhotel.html')

def kamarhotel_nodata_view(request):
    return render(request, 'kamarhotel_nodata.html')

def form_add_fasilitas_kamar_view(request):
    return render(request, 'form_tambah_fasilitas_kamar.html')

def form_add_kamar_view(request):
    return render(request, 'form_tambah_kamar.html')
