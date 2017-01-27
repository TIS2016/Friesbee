from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import smart_unicode
from django.template.defaultfilters import default
            
            
                

class KlubSaf(models.Model):


    nazov = models.CharField(max_length=50, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Klub SAF'
        app_label = "frisbee"

    def __str__(self):
        return self.nazov

    def __repr__(self):
        return self.nazov

    def __unicode__(self):
        return smart_unicode(self.nazov)
