from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import FileExtensionValidator
from PyPDF2 import PdfReader

# Create your models here.
class Order (models.Model):

    STATUS_CHOICES = (('pending', 'Zlecone'),('in_progress', 'Podjęte'),('Zakończone', 'Zakończone'),)

    
    orderTag= models.CharField(max_length=15, verbose_name='WZP')
    orderCompany = models.CharField(max_length=15, verbose_name='Firma')
    orderName = models.CharField(max_length=15, verbose_name='Produkt')
    orderQuantity = models.IntegerField(verbose_name='Ilość')
    orderDate = models.DateTimeField(auto_now=True, verbose_name='Data Utworzenia')
    orderManager = models.ForeignKey(User, on_delete= models.SET_DEFAULT, verbose_name='Autor Zlecenia', default=1)
    orderManual = models.BooleanField(default=False)
    orderVideo = models.BooleanField(default=False)
    orderStatus = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    file = models.FileField(upload_to='media/', null=True, blank=True, verbose_name="Plik", validators=[FileExtensionValidator(['pdf'])])
    url = models.UUIDField(default=uuid.uuid4, editable=False)
    
    class Meta:
        verbose_name = ("Zlecenie")
        verbose_name_plural = ("Zlecenia")

    def count_pages(self):
       with self.file.open() as pdf_file:
            pdf = PdfReader(pdf_file)
            return len(pdf.pages)