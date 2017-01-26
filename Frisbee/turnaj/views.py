#-*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,render_to_response
from .models import Turnaj
from zapas.models import Zapas
from tim.models import Tim
from kategoriaTurnaju.models import KategoriaTurnaju
import django_tables2 as tables
from django_tables2 import RequestConfig
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_unicode
from kategoria.models import Kategoria


class BaseSimpleTable(tables.Table):
    kategoria = tables.Column(verbose_name= 'Kategória',orderable=True)
    datum_od = tables.Column(verbose_name= 'Dátum od',orderable=True)
    datum_do = tables.Column(verbose_name= 'Dátum do',orderable=True)
    #report = tables.Column(verbose_name= 'Report',orderable=True)
    
    class Meta:
        model = Turnaj
        fields = ('kategoria','datum_od','datum_do')
        attrs = {"class": "paleblue"}
        orderable = True
        
    def render_kategoria(self,record):
        vysledok = ''
        pocet = 0
        for kategoria in record.kategoria:
            vysledok += smart_unicode(kategoria)
            pocet+=1
            if pocet != len(record.kategoria):
                vysledok+=', '
        if vysledok=='':
            return '—'
        return vysledok
    
    def render_zapasy(self,record):
        return mark_safe('<a href="'+reverse("zobraz_zapasy_turnaja", args=[record.id])+'">Zobraz</a>')

class SimpleTableKlikolNaStat(BaseSimpleTable):
    kategoria = tables.Column(verbose_name= 'Kategória',orderable=True)
    datum_od = tables.Column(verbose_name= 'Dátum od',orderable=True)
    datum_do = tables.Column(verbose_name= 'Dátum do',orderable=True)
    #report = tables.Column(verbose_name= 'Report',orderable=True)
    nazov = tables.LinkColumn('zobraz_timi_turnaja', args=[tables.A('id')], orderable=True, empty_values=(), verbose_name= 'Názov')
    mesto = tables.LinkColumn('zobraz_turnaje_mesta',args=[tables.A('mesto')],verbose_name= 'Mesto',orderable=True)
    zapasy = tables.LinkColumn('zobraz_zapasy_turnaja',args=[tables.A('id')], orderable=False, empty_values=(), verbose_name= 'Zápasy')
    
    class Meta:
        model = Turnaj
        fields = ('nazov','kategoria','datum_od','datum_do','mesto',)
        attrs = {"class": "paleblue"}
        orderable = True

class SimpleTableKlikolNaMesto(BaseSimpleTable):
    kategoria = tables.Column(verbose_name= 'Kategória',orderable=True)
    datum_od = tables.Column(verbose_name= 'Dátum od',orderable=True)
    datum_do = tables.Column(verbose_name= 'Dátum do',orderable=True)
    #report = tables.Column(verbose_name= 'Report',orderable=True)
    nazov = tables.LinkColumn('zobraz_timi_turnaja', args=[tables.A('id')], orderable=True, empty_values=(), verbose_name= 'Názov')
    stat = tables.LinkColumn('zobraz_turnaje_statu',args=[tables.A('stat')],verbose_name= 'Štát',orderable=True)
    zapasy = tables.LinkColumn('zobraz_zapasy_turnaja',args=[tables.A('id')], orderable=False, empty_values=(), verbose_name= 'Zápasy')
    
    class Meta:
        model = Turnaj
        fields = ('nazov','kategoria','datum_od','datum_do','stat')
        attrs = {"class": "paleblue"}
        orderable = True
        
class SimpleTable(BaseSimpleTable):
    kategoria = tables.Column(verbose_name= 'Kategória',orderable=True)
    datum_od = tables.Column(verbose_name= 'Dátum od',orderable=True)
    datum_do = tables.Column(verbose_name= 'Dátum do',orderable=True)
    #report = tables.Column(verbose_name= 'Report',orderable=True)
    nazov = tables.LinkColumn('zobraz_timi_turnaja', args=[tables.A('id')], orderable=True, empty_values=(), verbose_name= 'Názov')
    stat = tables.LinkColumn('zobraz_turnaje_statu',args=[tables.A('stat')],verbose_name= 'Štát',orderable=True)
    mesto = tables.LinkColumn('zobraz_turnaje_mesta',args=[tables.A('mesto')],verbose_name= 'Mesto',orderable=True)
    zapasy = tables.LinkColumn('zobraz_zapasy_turnaja',args=[tables.A('id')], orderable=False, empty_values=(), verbose_name= 'Zápasy')
    
    class Meta:
        model = Turnaj
        fields = ('nazov','kategoria','datum_od','datum_do', 'stat','mesto',)
        attrs = {"class": "paleblue"}
        orderable = True

class SimpleTable2(BaseSimpleTable):
    kategoria = tables.Column(verbose_name= 'Kategória',orderable=True)
    datum_od = tables.Column(verbose_name= 'Dátum od',orderable=True)
    datum_do = tables.Column(verbose_name= 'Dátum do',orderable=True)
    #report = tables.Column(verbose_name= 'Report',orderable=True)
    nazov = tables.LinkColumn('zobraz_timi_turnaja', args=[tables.A('id')], orderable=True, empty_values=(), verbose_name= 'Názov')
    stat = tables.LinkColumn('zobraz_turnaje_statu',args=[tables.A('stat')],verbose_name= 'Štát',orderable=True)
    mesto = tables.LinkColumn('zobraz_turnaje_mesta',args=[tables.A('mesto')],verbose_name= 'Mesto',orderable=True)
##    zapasy = tables.LinkColumn('zobraz_zapasy_turnaja',args=[tables.A('id')], orderable=False, empty_values=(), verbose_name= 'Zápasy')
    
    class Meta:
        model = Turnaj
        fields = ('nazov','kategoria','datum_od','datum_do', 'stat','mesto',)
        attrs = {"class": "paleblue"}
        orderable = True
        
        
def turnaj(request):
    button = mark_safe('''
    <form action="#" method="get">
    <link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
    <script src="//code.jquery.com/jquery-1.10.2.js"></script>
    <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
    <link rel="stylesheet" href="/resources/demos/style.css">
    <script>
    $(function() {
        $( "#start" ).datepicker({ dateFormat: 'dd/mm/yy', showOn: "both", buttonImage: "http://jqueryui.com/resources/demos/datepicker/images/calendar.gif", buttonImageOnly: true}).datepicker("setDate", -365);
        $( "#end" ).datepicker({ dateFormat: 'dd/mm/yy', showOn: "both", buttonImage: "http://jqueryui.com/resources/demos/datepicker/images/calendar.gif", buttonImageOnly: true }).datepicker("setDate", new Date());
    });
    </script>
  
    <p>
        From: <input type="text" id="start" name="start">
        To: <input type="text" id="end" name="end">
        <input type="submit" class="btn" value="Filter" name="mybtn">
    </p>
  
    </form>
    <br>
    
    ''')
    
    categories = Kategoria.objects.all()
    queryset = None
    if request.GET.get('mybtn') and request.GET.get("start") and request.GET.get("end"):
        od = request.GET.get("start")
        od = od.split("/")
        od = [od[2], od[1], od[0]]
        od = "-".join(od)
        do = request.GET.get("end")
        do = do.split("/")
        do = [do[2], do[1], do[0]]
        do = "-".join(do)
        queryset= Turnaj.objects.filter(datum_od__range=[od,do])
    else:
        queryset= Turnaj.objects.all()

    for turnaj in queryset:
        kategorieturnaju = KategoriaTurnaju.objects.filter(turnaj=turnaj.id)
        turnaj.kategoria = kategorieturnaju
    nazov = smart_unicode("Turnaje")
    table = SimpleTable(queryset)
    RequestConfig(request).configure(table)
    
    cname = request.POST.get("dropdown1")
    if cname is not None:
        catid = Kategoria.objects.filter(nazov=cname).values('id')[0]['id']
        if request.method == 'POST':
            turn_id = KategoriaTurnaju.objects.filter(kategoria_id=smart_unicode(catid))
            queryset2 = Turnaj.objects.filter(id__in = [i.turnaj_id for i in turn_id])
            for i in turn_id:
                cnames = Kategoria.objects.filter(id__in = [i.kategoria_id for i in turn_id])
                cnames = ''.join(str(e) for e in cnames)

        else:
            pass
    ##        queryset = Turnaj.objects.all()
        for turnaj in queryset2:
            kategorieturnaju = KategoriaTurnaju.objects.filter(turnaj=turnaj.id)
            turnaj.kategoria = kategorieturnaju
        table2 = SimpleTable(queryset2)
        RequestConfig(request).configure(table2)
    else:
        queryset2 = None
        cnames = "Vyberte kategóriu"
        table2 = None
    nazov = smart_unicode("Turnaje")
    try:
        obsah = mark_safe("<h1>" + nazov + "</h1><section>" + smart_unicode("Zobrazenie Turnajov pomocou dátumu a filtra") + "</section>")
    except IndexError:
        obsah = mark_safe("<h1>NEEXISTUJE KATEGORIA</h1>")
        table=Turnaj.objects.none()
    if queryset2 is None: 
        return render(request,"turnaj.html", {"table": table, "nazov":nazov,"obsah":obsah, "button":button,"cat":categories, "kat_name": cnames,})
    return render(request,"turnaj.html", {"table": table2, "nazov":nazov,"obsah":obsah, "button":button,"cat":categories, "kat_name": cnames,})
    
# Create your views here.

def filter_turnaj(request):
    categories = Kategoria.objects.all()
    cname = request.POST.get("dropdown1")
    catid = Kategoria.objects.filter(nazov=cname).values('id')[0]['id']
    if request.method == 'POST':
        turn_id = KategoriaTurnaju.objects.filter(kategoria_id=smart_unicode(catid))
        queryset = Turnaj.objects.filter(id__in = [i.turnaj_id for i in turn_id])
        for i in turn_id:
            cnames = Kategoria.objects.filter(id__in = [i.kategoria_id for i in turn_id])
    else:
        pass
##        queryset = Turnaj.objects.all()
    nazov = smart_unicode("Filtrovane turnaje")
    table = SimpleTable(queryset)
    RequestConfig(request).configure(table)
    try:
        obsah = mark_safe("<h1>" + nazov + "</h1><section>" + smart_unicode("Zobrazenie Turnajov podla Filtra") + "</section>")
    except IndexError:
        obsah = mark_safe("<h1>NEEXISTUJE KATEGORIA</h1>")
        table=Turnaj.objects.none()
    return render(request,"turnaj.html",{"table":table, "nazov":nazov, "obsah":obsah, "cat":categories, "kat_name":cnames,})


from tim.views import SimpleTableKlikolTurnaj
from zapas.views import SimpleTableOdTurnaja 

def zobraz_zapasy_turnaja(request,id):
    nazov = smart_unicode("Zápasy Turnaja")
    kategorieTurnajov = KategoriaTurnaju.objects.filter(turnaj=id)
    queryset = Zapas.objects.filter(kategoria_turnaju__in=kategorieTurnajov)
    table = SimpleTableOdTurnaja(queryset)
    turnaj = Turnaj.objects.filter(id=id)
    try:
        obsah = mark_safe("<h1>" + nazov + " " + smart_unicode(turnaj[0]) + "</h1><section>" + smart_unicode("Zobrazenie zápasou  Turnaja") + "</section>")
    except IndexError:
        obsah = mark_safe("<h1>NEEXISTUJU ZÁPASY PRE DANÝ TURNAJ</h1>")
        table=Zapas.objects.none()
    RequestConfig(request).configure(table)
    return render(request,"table.html", {"table": table,"nazov":nazov,"obsah":obsah})

def zobraz_timi_turnaja(request,id_turnaja):  
    nazov = smart_unicode("Tímy Turnaja")
    kat_id = KategoriaTurnaju.objects.filter(turnaj_id__in=id_turnaja)
    timy = Tim.objects.filter(kategoria_turnaju_id__in=kat_id)
    queryset = timy
    for turnaj in queryset:
        kategorieTurnajov = KategoriaTurnaju.objects.filter(turnaj=id_turnaja)
        turnaj.kategoria = kategorieTurnajov
    table = SimpleTableKlikolTurnaj(queryset)
    RequestConfig(request).configure(table)
    
    turnaj = Turnaj.objects.filter(id=id_turnaja)
    try:
        obsah = mark_safe("<h1>" + nazov + " " + smart_unicode(turnaj[0]) + "</h1><section" + smart_unicode("Zobrazenie Tímov  Turnaja ") + "</section>")
    except IndexError:
        obsah = mark_safe("<h1>NEEXISTUJU TÍMY PRE DANÝ TURNAJ</h1>")
    return render(request,"table.html", {"table": table,"nazov":nazov,"obsah":obsah})


def zobraz_turnaje_statu(request,stat):
    button = mark_safe('''
    <form action="#" method="get">
    <link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
    <script src="//code.jquery.com/jquery-1.10.2.js"></script>
    <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
    <link rel="stylesheet" href="/resources/demos/style.css">
    <script>
    $(function() {
        $( "#start" ).datepicker({ dateFormat: 'dd/mm/yy', showOn: "both", buttonImage: "http://jqueryui.com/resources/demos/datepicker/images/calendar.gif", buttonImageOnly: true}).datepicker("setDate", -365);
        $( "#end" ).datepicker({ dateFormat: 'dd/mm/yy', showOn: "both", buttonImage: "http://jqueryui.com/resources/demos/datepicker/images/calendar.gif", buttonImageOnly: true }).datepicker("setDate", new Date());
    });
    </script>
  
    <p>
        From: <input type="text" id="start" name="start">
        To: <input type="text" id="end" name="end">
        <input type="submit" class="btn" value="Filter" name="mybtn">
    </p>
  
    </form>
    ''')
    
    queryset = None
    if request.GET.get('mybtn') and request.GET.get("start") and request.GET.get("end"):
        od = request.GET.get("start")
        od = od.split("/")
        od = [od[2], od[1], od[0]]
        od = "-".join(od)
        do = request.GET.get("end")
        do = do.split("/")
        do = [do[2], do[1], do[0]]
        do = "-".join(do)
        queryset= Turnaj.objects.filter(stat=stat)
        queryset = queryset.filter(datum_od__range=[od,do])
    else:
        queryset= Turnaj.objects.filter(stat=stat)
    
    for turnaj in queryset:
        kategorieturnaju = KategoriaTurnaju.objects.filter(turnaj=turnaj.id)
        turnaj.kategoria = kategorieturnaju
    nazov = smart_unicode("Turnaje Štátu")
    table = SimpleTableKlikolNaStat(queryset)
    try:
        obsah = mark_safe("<h1>" + nazov + " " + smart_unicode(queryset[0].stat) + "</h1><section>" + smart_unicode("Zobrazenie turnajov v danom štáte") + "</section>")
    except IndexError:
        obsah = mark_safe("<h1>" + nazov + " " + stat + "</h1><section>" + smart_unicode("Zobrazenie turnajov v danom štáte") + "</section>")
    RequestConfig(request).configure(table)
    return render(request,"table.html", {"table": table,"nazov":nazov,"obsah":obsah, "button":button})  

def zobraz_turnaje_mesta(request,mesto):
    button = mark_safe('''
    <form action="#" method="get">
    <link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
    <script src="//code.jquery.com/jquery-1.10.2.js"></script>
    <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
    <link rel="stylesheet" href="/resources/demos/style.css">
    <script>
    $(function() {
        $( "#start" ).datepicker({ dateFormat: 'dd/mm/yy', showOn: "both", buttonImage: "http://jqueryui.com/resources/demos/datepicker/images/calendar.gif", buttonImageOnly: true}).datepicker("setDate", -365);
        $( "#end" ).datepicker({ dateFormat: 'dd/mm/yy', showOn: "both", buttonImage: "http://jqueryui.com/resources/demos/datepicker/images/calendar.gif", buttonImageOnly: true }).datepicker("setDate", new Date());
    });
    </script>
  
    <p>
        From: <input type="text" id="start" name="start">
        To: <input type="text" id="end" name="end">
        <input type="submit" class="btn" value="Filter" name="mybtn">
    </p>
  
    </form>
    ''')
    
    queryset = None
    if request.GET.get('mybtn') and request.GET.get("start") and request.GET.get("end"):
        od = request.GET.get("start")
        od = od.split("/")
        od = [od[2], od[1], od[0]]
        od = "-".join(od)
        do = request.GET.get("end")
        do = do.split("/")
        do = [do[2], do[1], do[0]]
        do = "-".join(do)
        queryset= Turnaj.objects.filter(mesto=mesto)
        queryset = queryset.filter(datum_od__range=[od,do])
    else:
        queryset= Turnaj.objects.filter(mesto=mesto)
    
    for turnaj in queryset:
        kategorieturnaju = KategoriaTurnaju.objects.filter(turnaj=turnaj.id)
        turnaj.kategoria = kategorieturnaju
    nazov = smart_unicode("Turnaje Mesta")
    table = SimpleTableKlikolNaMesto(queryset)
    RequestConfig(request).configure(table)

    try:
        obsah = mark_safe("<h1>" + nazov + " " + smart_unicode(queryset[0].mesto) + "</h1><section>" + smart_unicode("Zobrazenie turnajov v danom meste") + "</section>")
    except IndexError:
        obsah = mark_safe("<h1>" + nazov + " " + mesto + "</h1><section>" + smart_unicode("Zobrazenie turnajov v danom meste") + "</section>")
    return render(request,"table.html", {"table": table,"nazov":nazov,"obsah":obsah, "button":button})  

def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None
