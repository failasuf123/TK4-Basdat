from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from utils.query import *
from django.db import DatabaseError, connection


cursor = connection.cursor()

def register_customer(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        nohp = request.POST.get('phone')
        nik = request.POST.get('nik')

        with connection.cursor() as cursor:
            try:
                cursor.execute("insert into sistel.user values ('{}','{}','{}', '{}') "
                    .format(email,password,fname,lname))
                cursor.execute("insert into sistel.reservation_actor values ('{}','{}') "
                    .format(email,nohp))
                cursor.execute("insert into sistel.customer values ('{}','{}') "
                    .format(email,nik))
            except DatabaseError as e:
                print(e)
                msg = "Terjadi error! Pastikan semua sudah sesuai ketentuan"
                context = {'msg': msg}
                return render(request, 'register_customer.html', context)

    return render(request, 'register_customer.html', context)

def register_hotel(request):
    if request.method == 'POST':
        # Mendapatkan data dari form
        email = request.POST.get('email')
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        nohp =request.POST.get('notelp')
        hname =request.POST.get('hname')
        hbranch =request.POST.get('hbranch')
        nib =request.POST.get('nib')
        street =request.POST.get('jalan')
        district =request.POST.get('kecamatan')
        city =request.POST.get('kota')
        province =request.POST.get('provinsi')
        rating = 0

        with connection.cursor() as cursor:
            try:
                cursor.execute("insert into sistel.user values ('{}','{}','{}', '{}') "
                                               .format(email, password,fname,lname))
                cursor.execute("insert into sistel.reservation_actor values ('{}','{}') "
                    .format(email,nohp))
                cursor.execute("insert into sistel.hotel values ('{}','{}','{}', '{}', '{}', '{}', '{}', '{}', '{}') "
                    .format(email, hname, hbranch, nib, rating, street, district, city, province))
            except DatabaseError as e:
                print(e)
                msg = "Terjadi error! Pastikan semua sudah sesuai ketentuan"
                context = {'msg': msg}
                return render(request, 'register_hotel.html', context)
    return render(request, 'register_hotel.html', context)