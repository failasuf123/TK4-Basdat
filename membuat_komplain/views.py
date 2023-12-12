from django.shortcuts import render, redirect
from django.db import connection, DatabaseError
from django.contrib import messages


# Create your views here.
def show_komplain_form(request):
    # Email dummy bypass login
    custemail = 'rizard0@youku.com'
    with connection.cursor() as cursor:
        cursor.execute("""
select u.fname, u.lname from user_sistel u
where u.email = %s""", [custemail])
        user_info = cursor.fetchone()

    context = {
        'email': custemail,
        'nama': user_info[0] + " " + user_info[1],
    }

    return render(request, 'formkomplain.html', context)

def mengajukan_komplain(request):
    if request.method == 'POST':
        cust_email = request.POST.get('cust_email')
        complaint = request.POST.get('complaint_details')

        with connection.cursor() as cursor:
            cursor.execute("""
select count(*) from complaints""")
            id_now = "C" + str(cursor.fetchone()[0]+1)

            cursor.execute("""
select r.rid from reservation r
join reservation_room rr on r.rid = rr.rsv_id
where r.cust_email = %s and
rr.isactive is TRUE limit 1""", [cust_email])
            rsv_id = cursor.fetchone()

            try:
                cursor.execute("""
insert into complaints values (%s, %s, %s, %s)""", [id_now, cust_email, rsv_id, complaint])
            except DatabaseError as e:
                error_messages = str(e)
                messages.error(request, error_messages)
                return redirect('dashboard:show_dashboard_customer')
            
        return redirect('dashboard:show_dashboard_customer')