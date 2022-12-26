from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Spek

class SpekForms(forms.ModelForm):
    class Meta:
        model = Spek
        fields = ('produk', 'detail', 'merk')
        widgets = {
            "produk" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Nama Produk',
                    'required': True,
                }),
            "detail" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Isi Detail',
                    'cols':'30',
                    'rows':'10',
                    'required': True,
                }),
            "merk" : forms.Select(
                attrs={
                    'class': 'selectpicker',
                    'required': True,
                    'data-style':'btn btn-danger btn-block',
                    'title':'Pilih Merk', 
                    'data-size':'7',
                }),     
        }