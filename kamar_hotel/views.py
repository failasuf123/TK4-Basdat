from django.shortcuts import render,redirect
from utils.query import *
from django.db import connection


cursor = connection.cursor()

# def fetch_data(query):
#     if query.description:
#         columns = [col[0] for col in query.description]
#         return [dict(zip(columns, row)) for row in query.fetchall()]
#     else:
#         return []
    

# def kamarhotel_view(request):
#     query = cursor.execute(f"""
#      SELECT R.hotel_name,R.price, R.floor, HF.facility_name
#     FROM ROOM R
#     JOIN HOTEL H ON R.hotel_name = H.hotel_name AND R.hotel_branch = H.hotel_branch
#     JOIN hotel_facilities HF ON HF.hotel_name = H.hotel_name AND HF.hotel_branch = H.hotel_branch;
#     """)
#     record = cursor.fetchall()
#     daftar_kamar_hotel = fetch_data(query)

#     context = {'data_kamar' : daftar_kamar_hotel}
   
#     return render(request, 'kamarhotel.html',context)

def kamarhotel_view(request):
    query = cursor.execute("""
     SELECT R.hotel_name, R.price, R.floor, HF.facility_name
     FROM ROOM R
     JOIN HOTEL H ON R.hotel_name = H.hotel_name AND R.hotel_branch = H.hotel_branch
     JOIN hotel_facilities HF ON HF.hotel_name = H.hotel_name AND HF.hotel_branch = H.hotel_branch;
    """)
    record = cursor.fetchall()

    context = {'data_kamar': record}

    return render(request, 'kamarhotel.html', context)

def kamarhotel_nodata_view(request):
    return render(request, 'kamarhotel_nodata.html')

def form_add_fasilitas_kamar_view(request):
    return render(request, 'form_tambah_fasilitas_kamar.html')

def form_add_kamar_view(request):
    return render(request, 'form_tambah_kamar.html')
