from django.urls import path
from membuat_komplain.views import show_komplain_form, mengajukan_komplain

app_name = 'membuat_komplain'

urlpatterns = [
    path('', show_komplain_form, name='show_komplain_form'),
    path('mengajukan/', mengajukan_komplain, name='mengajukan_komplain'),
]