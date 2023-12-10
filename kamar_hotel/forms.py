# forms.py
from django import forms

class KamarHotelForm(forms.Form):
    nomor_kamar = forms.CharField(
        label="Nomor Kamar",
        widget=forms.TextInput(attrs={'class': 'form-input mt-1 p-2 w-full border rounded'}),
    )
    harga = forms.CharField(
        label="Harga",
        widget=forms.TextInput(attrs={'class': 'form-input mt-1 p-2 w-full border rounded'}),
    )
    lantai = forms.IntegerField(
        label="Lantai",
        widget=forms.NumberInput(attrs={'class': 'form-input mt-1 p-2 w-full border rounded'}),
    )
