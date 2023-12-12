from django.shortcuts import render, redirect
from django.db import connection

# Create your views here.
def show_dashboard_customer(request):
    
    # if 'cust_email' not in request.session:
    #     return redirect('otentikasi:login_view')
    
    # email = request.session.get('cust_email')

    # email dummy bypass login
    email = 'rizard0@youku.com'
    with connection.cursor() as cursor:
        cursor.execute("""
select u.fname, u.lname, ra.phonenum, u.email, c.nik from user_sistel u
join reservation_actor ra on u.email = ra.email
join customer c on u.email = c.email
where u.email = %s""", [email])
        user_info = cursor.fetchone()

    context = {
        'first_name': user_info[0],
        'last_name': user_info[1],
        'phone_num': user_info[2],
        'email': user_info[3],
        'nik': user_info[4]
    }

    return render(request, "dashboardCustomer.html", context)

def show_dashboard_hotel(request):
    # if 'hotel_email' not in request.session:
    #     return redirect('otentikasi:login_view')
    
    # htl_email = request.session.get('hotel_email')

    # dummy email bypass login
    htl_email = 'mgregoraciz@admin.ch'
    with connection.cursor() as cursor:
        cursor.execute("""
select u.fname, u.lname, ra.phonenum, u.email, h.nib, h.hotel_name, h.hotel_branch,
h.street, h.district, h.city, h.province from user_sistel u
join reservation_actor ra on u.email = ra.email
join hotel h on u.email = h.email
where u.email = %s;""", [htl_email])
        hotel_info = cursor.fetchone()

        cursor.execute("""
select hf.facility_name from hotel_facilities hf
where hf.hotel_name = %s and
hf.hotel_branch = %s""", [hotel_info[5], hotel_info[6]])
        facilities = cursor.fetchall()

        cursor.execute("""
select rf.rnum, r.price, r.floor, string_agg(distinct(rf.id), ', ') from room_facilities rf
join room r on r.hotel_name = rf.hotel_name and r.hotel_branch = rf.hotel_branch
where r.hotel_name = %s and
r.hotel_branch = %s
group by rf.rnum, r.price, r.floor""", [hotel_info[5], hotel_info[6]])
        rooms = cursor.fetchall()


    context = {
        'nama_pemilik': hotel_info[0] + " " + hotel_info[1],
        'nomor_hp': hotel_info[2],
        'email': hotel_info[3],
        'nib': hotel_info[4],
        'nama_hotel': hotel_info[5] + " " + hotel_info[6],
        'alamat': hotel_info[7] + ", " + hotel_info[8] + ", " + hotel_info[9] + ", " + hotel_info[10] 
    }

    full_content = {'facilities': facilities, 'rooms':rooms, **context}

    return render(request, "dashboardHotel.html", full_content)