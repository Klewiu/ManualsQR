from django.db import models
from django.contrib.auth.models import User

class Marketing (models.Model):
    label = models.CharField(max_length=15, verbose_name='Tytuł slajdu', null=True, blank=True)
    caption = models.CharField(max_length=15, verbose_name='Tekst slajdu', null=True, blank=True)
    slide = models.FileField(upload_to='marketing',  verbose_name="Grafika slajdu", default='/default_slide.png')
   
    class Meta:
        verbose_name = ("Baner Marketingowy")
        verbose_name_plural = ("Banery Marketingowe")
