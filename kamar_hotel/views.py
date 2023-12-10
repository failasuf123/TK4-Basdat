from django.shortcuts import render,redirect
from utils.query import *
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect


# cursor = connection.cursor()

def kamarhotel_view(request):
    try:
        email = request.COOKIES.get('email')
    except:
        email = 'dboyack14@wikia.com'
    email = 'dboyack14@wikia.com'
    cursor.execute("""
    SELECT R.hotel_name, R.price, R.floor, HF.facility_name
    FROM ROOM R
    JOIN HOTEL H ON R.hotel_name = H.hotel_name AND R.hotel_branch = H.hotel_branch
    JOIN hotel_facilities HF ON HF.hotel_name = H.hotel_name AND HF.hotel_branch = H.hotel_branch
    WHERE H.email = %(email)s
    ;
    """, {'email': email})
    record = cursor.fetchall()
    context = {
        "record": record
    }
    
    if len(record) > 0:
        context = {'data_kamar': record}
        # for n in context:
        #     print(n)
        return render(request, 'kamarhotel.html', context)
    else:
        return render(request, 'kamarhotel_nodata.html')

def kamarhotel_nodata_view(request):
    return render(request, 'kamarhotel_nodata.html')

def form_add_fasilitas_kamar_view(request):
    return render(request, 'form_tambah_fasilitas_kamar.html')

def form_add_kamar_view(request):
    return render(request, 'form_tambah_kamar.html')
