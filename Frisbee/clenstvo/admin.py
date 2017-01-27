from django.contrib import admin
from django.contrib.auth.models import User
import nested_admin
from models import Clenstvo

# Register your models here.

class ClenstvoAdminSelf(nested_admin.NestedAdmin):
    list_display = ['hrac_id','klub_saf_id','datum_platby','zaplateny_za_rok','suma']
    list_filter = ['hrac','zaplateny_za_rok','klub_saf_id']
    search_fields = ['datum_platby','hrac']

admin.site.register(Clenstvo, ClenstvoAdminSelf)


