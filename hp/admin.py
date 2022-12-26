from django.contrib import admin
from .models import *
# Register your models here.

class SpekAdmin(admin.ModelAdmin):
    list_display = ('nama','produk','detail','merk','date')
class InfoAdmin(admin.ModelAdmin):
    list_display = ('nama','produk','detail','nomor','count','date')    

admin.site.register(Merk)
admin.site.register(Spek, SpekAdmin)
admin.site.register(Info, InfoAdmin)