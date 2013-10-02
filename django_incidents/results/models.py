# Create your models here.
# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from django.db import models

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating
    ``created`` and ``modified`` fields. following @pydanny
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class IncidentType(models.Model):
    """
    Klasa typ incydentu
    """
    name = models.CharField(max_length=255, verbose_name=u'Nazwa')
    active = models.BooleanField(verbose_name=u'Aktywne ?')

    def __unicode__(self):
        return self.name

class Incident(TimeStampedModel):
    """
    Klasa zgłoszenia
    """
    start_date = models.DateTimeField(verbose_name=u'Data i czas rozpoczęcia')
    end_date = models.DateTimeField(verbose_name=u'Data i czas zakończenia')
    street = models.CharField(max_length=255, verbose_name=u'Ulica')
    street_nr = models.CharField(max_length=5, verbose_name=u'Numer')
    lat = models.FloatField(verbose_name='Latitude', blank=True, null=True)
    lon = models.FloatField(verbose_name='Longitude', blank=True, null=True)
    description = models.TextField(verbose_name=u'Opis', blank=True)
    incident_type = models.ForeignKey(IncidentType, verbose_name=u'Typ zdarzenia')
    inv = models.BooleanField(verbose_name=u'Wezwanie ?')
    inv_number = models.CharField(max_length=15, unique=True, verbose_name=u'Numer wezwania')
    inv_cepik = models.BooleanField(default=True, verbose_name=u'Zapytanie Cepik')

    def __unicode__(self):
        return u'{0} {1} {2} {3}'.format(
            user.first_name,
            user.last_name,
            self.lan,
            self.lon
        )





