from django.urls import path ,include
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('spek/', spek, name='tabel_spek'),
    path('info/', info, name='tabel_info'),
    path('spek/tambah', tambah_spek, name='tambah_spek'),
    path('sinkron_hp', sinkron_hp, name='sinkron_hp'),
    path('spek/lihat/<str:id>', lihat_spek, name='lihat_spek'),
    path('spek/edit/<str:id>', edit_spek, name='edit_spek'),
    path('spek/delete/<str:id>', delete_spek, name='delete_spek'),
    path('info/delete/<str:id>', delete_info, name='delete_info'),

    path('users/', users, name='tabel_users'),

]