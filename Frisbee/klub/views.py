# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from .models import Klub
from hrac.models import Hrac
from hrac.views import SimpleTable as SimpleTableHrac
import django_tables2 as tables
from django_tables2 import RequestConfig
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_unicode
from django.template import RequestContext

class SimpleTable(tables.Table):
    nazov = tables.LinkColumn('hraci_klubu', args=[tables.A('id')], orderable=True, empty_values=(), verbose_name= 'Názov')
    pocet_hracov = tables.Column(verbose_name='Počet hráčov', orderable=True)
    pocet_vyhier = tables.Column(verbose_name='Počet výhier', orderable=True)
    pocet_prehier = tables.Column(verbose_name='Počet prehier', orderable=True)
    spirit = tables.Column(verbose_name='Spirity',orderable=True, empty_values=())
    
    
    class Meta:
        model = Klub
        fields = ('nazov', 'pocet_hracov', 'pocet_vyhier', 'pocet_prehier', 'spirit' ,)
        attrs = {"class": "paleblue"}
        orderable = True

# Create your views here.
def klub(request):
    nazov = "Kluby"
    queryset = Klub.objects.all()
    klubs = Klub.objects.all()
    table = SimpleTable(queryset)
    RequestConfig(request).configure(table)
    obsah = mark_safe("<h1>" + nazov + "</h1><section>" + smart_unicode('Zobrazenie všetkých Klubov.') + " " + smart_unicode('Pre zobrazenie klikni na klub')+" </section>")
    return render(request,"klub.html", {"table": table,"nazov":nazov,"obsah":obsah,"klubs":klubs})
