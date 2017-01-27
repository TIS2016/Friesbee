from django.db import models

# Create your models here.

from django.utils.encoding import smart_unicode
from django.template.defaultfilters import default


class TypClenstva(models.Model):
     
    nazov = models.CharField(max_length = 20,null=True, blank=True)
    suma = models.DecimalField(decimal_places=3,max_digits = 5,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Typ Clenstva'
        app_label = "frisbee"
