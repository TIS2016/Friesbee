from django.contrib import admin

from models import TypClenstva

# Register your models here.

class TypClenstvaAdminSelf(admin.ModelAdmin):
    list_display = ['nazov','suma']
    search_fields = ['nazov','suma']

admin.site.register(TypClenstva,TypClenstvaAdminSelf)
