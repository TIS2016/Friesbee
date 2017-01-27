from django.contrib import admin
import nested_admin
from models import KlubSaf

class KlubSafAdminSelf(nested_admin.NestedAdmin):
    list_display = ['nazov']
    search_fields = ['nazov']


admin.site.register(KlubSaf, KlubSafAdminSelf)
    
