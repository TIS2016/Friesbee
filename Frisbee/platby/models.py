#-*- coding: utf-8 -*-
from django.db import models

##from klub.models import Klub
##from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from django.template.defaultfilters import default
from datetime import date
from hrac.models import Hrac
from kategoriaPlatieb.models import KategoriaPlatieb


class Platba(models.Model):
    percenty = (
        (smart_unicode("10%"),smart_unicode("10%")),
        (smart_unicode("20%"),smart_unicode("20%")),
        (smart_unicode("30%"),smart_unicode("30%")),
        (smart_unicode("40%"),smart_unicode("40%")),
        (smart_unicode("50%"),smart_unicode("50%")),
        (smart_unicode("60%"),smart_unicode("60%")),
        (smart_unicode("70%"),smart_unicode("70%")),
        (smart_unicode("80%"),smart_unicode("80%")),
        (smart_unicode("90%"),smart_unicode("90%")),
        (smart_unicode("100%"),smart_unicode("100%")),
    
        )
    
    datum_platby = models.DateField(default=date.today, null=True, blank=True)
    celkova_suma= models.CharField(max_length = 50, null=True, blank=True, default="2000€")
    percent = models.CharField(max_length=5, choices = percenty, default = "100%", null=True, blank=True)
    hrac = models.ForeignKey(Hrac, null=True, blank=True)
    kategoria_platby = models.ForeignKey(KategoriaPlatieb, null=True, blank=True,)


    class Meta:
        verbose_name_plural = 'Platby'
        app_label = "frisbee"
