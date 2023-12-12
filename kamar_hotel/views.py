import os
from django.shortcuts import render,redirect
from utils.query import *
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
# from supabase import create_client, Client

def kamarhotel_view(request):
    try:
        email = request.COOKIES.get('email')
    except:
        email = 'dboyack14@wikia.com'
    email = 'dboyack14@wikia.com'
    cursor.execute("""
    select
        R.number,
        R.hotel_name,
        R.hotel_branch,
        R.price,
        R.floor,
        coalesce(string_agg(distinct RF.id, ','), 'no facility') as facility_names
    from
        ROOM R
        join HOTEL H on R.hotel_name = H.hotel_name
        and R.hotel_branch = H.hotel_branch
        join hotel_facilities HF on HF.hotel_name = H.hotel_name
        and HF.hotel_branch = H.hotel_branch
        left join room_facilities RF on RF.hotel_name = R.hotel_name
        and RF.hotel_branch = R.hotel_branch
        and RF.rnum = R.number
    where
        H.email =  %(email)s
    group by
        R.number,
        R.hotel_name,
        R.hotel_branch,
        R.price,
        R.floor;
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


def form_add_fasilitas_kamar_view(request,id):
    try:
        email = request.COOKIES.get('email')
    except:
        email = 'dboyack14@wikia.com'

    email = 'dboyack14@wikia.com'

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
        number = id
        nama_fasilitas = request.POST.get('nama_fasilitas')

        # Lakukan query untuk menambahkan room setelah mendefinisikan connection
        try:
            cursor.execute("""
                INSERT INTO room_facilities (hotel_name, hotel_branch, rnum, id, distance)
                VALUES (%s, %s, %s, %s, %s)
            """, [hotel_name, hotel_branch, number, nama_fasilitas, number])

            # Commit perubahan ke database
            connection.commit()

            connection.close()


            # Redirect ke halaman yang sesuai setelah menambahkan room
            return redirect('/kamarhotel/')
        except Exception as e:
            # Tangani kesalahan jika query tidak berhasil
            print(e)
            return render(request, 'error.html', {'error_message': 'Gagal menambahkan room'})


    return render(request, 'form_tambah_fasilitas_kamar.html')

def delete(request, id):
    try:
        cursor.execute("""
                delete from room where number = %(id)s;
        """, (id), {'confirm': True})
        connection.commit()
        connection.close()


    except Exception as e:
        print(e)
        return render(request, 'error.html', {'error_message': 'Gagal Add Data'})


    
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
        price = int(request.POST.get('harga'))
        floor = int(request.POST.get('lantai'))


        # query2 = f"""
        #      INSERT INTO ROOM ({hotel_name}, {hotel_branch}, {number}, {price},{floor});
        #         """

        # Lakukan query untuk menambahkan room setelah mendefinisikan connection
        try:
            # cursor.execute(query2)
            cursor.execute("""
                INSERT INTO room (hotel_name, hotel_branch, number, price, floor)
                VALUES (%s, %s, %s, %s, %s)
            """, (hotel_name, hotel_branch, number, price, floor))

            # Commit perubahan ke database
            connection.commit()
            connection.close()

            # Redirect ke halaman yang sesuai setelah menambahkan room
            return redirect('/kamarhotel/')
        except Exception as e:
            # Tangani kesalahan jika query tidak berhasil
            print(e)
            return render(request, 'error.html', {'error_message': 'Gagal menambahkan room'})

    return render(request, 'form_tambah_kamar.html')

# def delete(request, id):
#     try:
#         response = supabase.from_("room").delete().match({"number": id}).confirm("Hapus kamar ini?").execute()
#         # Periksa response untuk memastikan data telah dihapus
#         if response.data is None:
#             return redirect('/kamarhotel/')
#         else:
#             # Tangani error jika data tidak dihapus
#             pass
#     except Exception as e:
#         print(e)
#         return render(request, 'error.html', {'error_message': 'Gagal Hapus Data'})
