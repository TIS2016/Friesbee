
#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import time

from klub.models import Klub
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from django.template.defaultfilters import default
from datetime import date
from hrac.models import Hrac
from klubSaf.models import KlubSaf
from typClenstva.models import TypClenstva



def roky(datum):
    return [i for i in range(int(datum.year),int(datum.year)+6,1)]

class Clenstvo(models.Model):
    rok = roky(date.today())
    typy = TypClenstva.objects.all()
    pole = []
    for i in typy:
        pole.append(i.nazov)
    datum_platby = models.DateField(default=date.today, null=True, blank=True)
    suma = models.DecimalField(decimal_places=3,max_digits=5,default = '13', null=True, blank=True)
    zaplateny_za_rok = models.IntegerField(default=rok[0], choices = [(i,smart_unicode(i)) for i in rok], null=False, blank=True)
    hrac = models.OneToOneField(Hrac, null=True, blank=True)
    klub_saf_id = models.ForeignKey(KlubSaf, null=True, blank=True)
    typ_clenstva = models.CharField(max_length=30,choices = [(i,smart_unicode(i)) for i in pole],null=True, blank=True)



    class Meta:
        verbose_name_plural = 'Clenstvo'
        app_label = "frisbee"

    def __str__(self):
	return str(self.suma)

    def __repr__(self):
	return self.suma


        
