from re import template
import re
from django.http import request
from django.shortcuts import render, redirect
from multiprocessing import context
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.models import User

from .models import Spek, Merk,Info
from .forms import SpekForms
import requests

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'

    template_name = "back/dashboard.html"
    context = {
        'title' : 'dashboard'
    }
    return render(request, template_name, context)

@login_required
def spek(request):
    template_name = "back/tabel_spek.html"
    spek = Spek.objects.all()
    context = {
        'title' : 'tabel spek hp',
        'spek':spek,
    }
    return render(request, template_name, context)

def info(request):
    template_name = "back/tabel_info.html"
    info = Info.objects.all()
    context = {
        'title' : 'tabel info hp',
        'info':info,
    }
    return render(request, template_name, context)

@login_required
def tambah_spek(request):
    template_name = "back/tambah_spek.html"
    merk = Merk.objects.all()
    
    if request.method == "POST":
        forms_spek = SpekForms(request.POST)
        if forms_spek.is_valid():
            art = forms_spek.save(commit=False)
            art.nama = request.user 
            art.save()
            return redirect(spek)
    else:
        forms_spek = SpekForms()
    context = {
        'title' : 'tambah spek',
        'merk':merk,
        'forms_spek':forms_spek,
    }
    return render(request, template_name, context)

@login_required
def lihat_spek(request, id):
    template_name = "back/lihat_spek.html"
    spek = Spek.objects.get(id=id)
    context = { 
        'title' : 'lihat spek',
        'spek'  : spek,
    }
    return render(request, template_name, context)

@login_required
def edit_spek(request, id):
    template_name = "back/tambah_spek.html"
    s = Spek.objects.get(id=id)
    if request.method == "POST":
        forms_spek = SpekForms(request.POST, instance=s)
        if forms_spek.is_valid():
            art = forms_spek.save(commit=False)
            art.nama = request.user
            art.save()
            return redirect(spek)
    else:
        forms_spek = SpekForms(instance=s)
    context = { 
        'title' : 'Edit Spek',
        'spek'  : s,
        'forms_spek':forms_spek
    }
    return render(request, template_name, context)

@login_required
def delete_spek(request, id):
    Spek.objects.get(id=id).delete()
    return redirect(spek)
@login_required
def delete_info(request, id):
    Info.objects.get(id=id).delete()
    return redirect(spek)

@login_required
@user_passes_test(is_operator)
def users(request):
    template_name = "back/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title' : 'tabel users',
        'list_user':list_user
    }
    return render(request, template_name, context)

def sinkron_hp(request):
    url = "http://phone-specs-api.azharimm.dev/brands"
    data = requests.get(url).json()
    for d in data['data']:
            cek_berita = Info.objects.filter(nomor=d['brand_id'])
            if cek_berita:
                print('data sudah ada')
                c = cek_berita.first()
                c.nomor=d['brand_id']
                c.save()
            else: 
                #jika belum ada maka tulis baru kedatabase
                b = Info.objects.create(
                    nomor = d['brand_id'],
                    nama = d['brand_name'],
                    produk = d['brand_slug'],
                    count = d['device_count'],
                    detail = d['detail'],
                )
    return redirect(info)    
