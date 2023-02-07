from django.db import models
from django.contrib.auth.models import User

class Marketing (models.Model):
    label = models.CharField(max_length=40, verbose_name='Tytuł slajdu')
    slide = models.FileField(upload_to='marketing',  verbose_name="Grafika slajdu",null=True, blank=True)
   
    class Meta:
        verbose_name = ("Baner Marketingowy")
        verbose_name_plural = ("Banery Marketingowe")
