from django.db import models
from django.core.exceptions import ValidationError
from django import forms

# Create your models here.
class Notifications(models.Model):
    email = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Powiadomienie'
        verbose_name_plural = 'Powiadomienia'