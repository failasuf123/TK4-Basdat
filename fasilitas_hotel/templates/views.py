from django.shortcuts import render,redirect
from utils.query import *
from django.db import connection


cursor = connection.cursor()

def fasilitashotel_view(request):
    query = cursor.execute("""
    SELECT HF.facility_name
    FROM HOTEL_FACILITIES HF
    JOIN HOTEL H ON H.hotel_name = HF.hotel_name AND H.hotel_branch = HF.hotel_branch
    """)

    record = cursor.fetchall()

    context = {'data_fasilitas': record}

    return render(request, 'fasilitashotel.html', context)

def fasilitashotel_nodata_view(request):
    return render(request, 'fasilitashotel_nodata.html')

def form_add_fasilitas_view(request):
    return render(request, 'form_tambah_fasilitas.html')