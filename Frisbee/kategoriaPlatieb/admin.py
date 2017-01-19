from django.contrib import admin

from models import KategoriaPlatieb

# Register your models here.

class KategoriaPlatiebAdminSelf(admin.ModelAdmin):
    list_display = ['nazov']
    search_fields = ['nazov']

admin.site.register(KategoriaPlatieb,KategoriaPlatiebAdminSelf)
