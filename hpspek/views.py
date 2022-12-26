from hp.models import Spek
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.db import  transaction
from django.contrib.auth.hashers import make_password

from user.models import Biodata
import requests
from hp.models import Spek

def home(request):
    url = "http://phone-specs-api.azharimm.dev/brands"

    data = requests.get(url).json()

    a = data['data']
    nomor = []
    name = []
    slug = []
    count = []
    detail = []
    

    for i in range(len(a)):
        f = a[i]
        nomor.append(f['brand_id'])
        name.append(f['brand_name'])
        slug.append(f['brand_slug'])
        count.append(f['device_count'])
        detail.append(f['detail'])


    mylist = zip(nomor, name, slug, count,detail)
    context ={'mylist':mylist}

    return render(request, 'front/home.html', context)

def about(request):
    template_name = 'front/about.html'
    context = {
        'title':'About Us'
    }
    return render(request, template_name, context)

def contact(request):
    template_name = 'front/contact.html'
    context = {
        'title':'Contact Us'
    }
    return render(request, template_name, context)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    template_name = 'account/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #data ada
            print('username benar')
            auth_login(request, user)
            return redirect('home')
        else:
            #data tidak ada
            print('username salah')
    context = {
        'title':'Form Login'
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('home')\

def register(request):
    template_name = 'account/register.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')
        telp = request.POST.get('telp')

        try:
            with transaction.atomic():
                User.objects.create(
                    username = username,
                    password = make_password(password),
                    first_name = nama_depan,
                    last_name= nama_belakang,
                    email = email
                )
                get_user = User.objects.get(username = username)
                Biodata.objects.create(
                    user = get_user,
                    alamat = alamat,
                    telp = telp,
                )
            return redirect(home)
        except:pass
        print(username,password,nama_depan,nama_belakang,email,alamat,telp)
    context = {
        'title':'form register',
    }
    return render(request, template_name, context)