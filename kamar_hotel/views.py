from django.shortcuts import render,redirect
from utils.query import *
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from .forms import KamarHotelForm


def kamarhotel_view(request):
    try:
        email = request.COOKIES.get('email')
    except:
        email = 'dboyack14@wikia.com'
    email = 'dboyack14@wikia.com'
    cursor.execute("""
    SELECT R.number, R.hotel_name, R.price, R.floor, HF.facility_name
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
        return render(request, 'kamarhotel.html', context)
    else:
        return render(request, 'kamarhotel_nodata.html')


def form_add_fasilitas_kamar_view(request):
    return render(request, 'form_tambah_fasilitas_kamar.html')


def form_add_kamar_view(request):
    try:
        email = request.COOKIES.get('email')
    except:
        email = 'dboyack14@wikia.com'

    email = 'dboyack14@wikia.com'

    # Mendapatkan objek kursor setelah mendefinisikan connection
    
    if request.method == 'POST':
        cursor.execute("""
            SELECT distinct H.hotel_name, H.hotel_branch
            FROM ROOM R
            JOIN HOTEL H ON R.hotel_name = H.hotel_name AND R.hotel_branch = H.hotel_branch
            JOIN hotel_facilities HF ON HF.hotel_name = H.hotel_name AND HF.hotel_branch = H.hotel_branch
            WHERE H.email = %(email)s;
        """, {'email': email})
        records = cursor.fetchall()

        hotel_name = records[0][0] 
        hotel_branch = records[0][1]
        number = request.POST.get('nomor_kamar')
        price = request.POST.get('harga')
        floor = request.POST.get('lantai')

        # Lakukan query untuk menambahkan room setelah mendefinisikan connection
        try:
            cursor.execute("""
                INSERT INTO room (hotel_name, hotel_branch, number, price, floor)
                VALUES (%s, %s, %s, %s, %s)
            """, [hotel_name, hotel_branch, number, price, floor])

            # Commit perubahan ke database
            connection.commit()

            # Redirect ke halaman yang sesuai setelah menambahkan room
            return redirect('/kamarhotel/')
        except Exception as e:
            # Tangani kesalahan jika query tidak berhasil
            print(e)
            return render(request, 'error.html', {'error_message': 'Gagal menambahkan room'})

    return render(request, 'form_tambah_kamar.html')


