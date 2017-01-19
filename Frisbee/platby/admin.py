from django.contrib import admin
from django.contrib.auth.models import User
import nested_admin
from models import Platba

# Register your models here.

class PlatbyAdminSelf(nested_admin.NestedAdmin):
    list_display = ['hrac_id','kategoria_platby','datum_platby','celkova_suma', 'percent']
    list_filter = ['hrac','kategoria_platby',]
    search_fields = ['datum_platby','percent','hrac']

admin.site.register(Platba, PlatbyAdminSelf)


