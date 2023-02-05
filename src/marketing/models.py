from django.db import models
from django.contrib.auth.models import User

class Marketing (models.Model):
    firstLabel = models.CharField(max_length=15, verbose_name='Tytuł pierwszego slajdu')
    firstCaption = models.CharField(max_length=15, verbose_name='Tekst pierwszego slajdu')
    secondLabel = models.CharField(max_length=15, verbose_name='Tytuł drugiego slajdu')
    secondCaption = models.CharField(max_length=15, verbose_name='Tekst drugiego slajdu')
    thirdLabel = models.CharField(max_length=15, verbose_name='Tytuł trzeciego slajdu')
    thirdCaption = models.CharField(max_length=15, verbose_name='Tekst trzeciego slajdu')
    firstSlide = models.FileField(upload_to='marketing', null=True, blank=True, verbose_name="Pierwszy slajd")
    secondSlide = models.FileField(upload_to='marketing', null=True, blank=True, verbose_name="Drugi slajd")
    thirdSlide = models.FileField(upload_to='marketing', null=True, blank=True, verbose_name="Trzeci slajd")

    class Meta:
        verbose_name = ("Baner Markegin")
        verbose_name_plural = ("Banery Marketingowe")
