from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import FileExtensionValidator
from PyPDF2 import PdfReader

# Create your models here.
class Order (models.Model):

    STATUS_CHOICES = (('Zlecone', 'Zlecone'),('Podjęte', 'Podjęte'),('Zakończone', 'Zakończone'),)

    
    orderTag= models.CharField(max_length=15, verbose_name='WZP')
    orderCompany = models.CharField(max_length=15, verbose_name='Firma')
    orderName = models.CharField(max_length=15, verbose_name='Produkt')
    orderQuantity = models.IntegerField(verbose_name='Ilość')
    orderDate = models.DateTimeField(auto_now=True, verbose_name='Data Utworzenia')
    orderManager = models.ForeignKey(User, on_delete= models.SET_DEFAULT, verbose_name='Autor Zlecenia', default=1)
    orderManual = models.BooleanField(default=False)
    orderVideo = models.BooleanField(default=False)
    orderStatus = models.CharField(max_length=20, choices=STATUS_CHOICES)
    file = models.FileField(upload_to='media/', null=True, blank=True, verbose_name="Instrukcja PL", validators=[FileExtensionValidator(['pdf'])])
    file2 = models.FileField(upload_to='media/', null=True, blank=True, verbose_name="Instrukcja ENG", validators=[FileExtensionValidator(['pdf'])])
    video = models.TextField(max_length=10000, verbose_name='Multimedia/Video Embed')
    url = models.UUIDField(default=uuid.uuid4, editable=False)
    
    class Meta:
        verbose_name = ("Zlecenie")
        verbose_name_plural = ("Zlecenia")

    def count_pages_file1(self):
        pages1 = 0
        if self.file:
            with self.file.open() as pdf_file:
                pdf = PdfReader(pdf_file)
                pages1 += len(pdf.pages)
        return pages1
    
    def count_pages_file2(self):
        pages2 = 0
        if self.file2:
            with self.file2.open() as pdf_file:
                pdf = PdfReader(pdf_file)
                pages2 += len(pdf.pages)
        return pages2

    # Function counts the pages of added PDF file #
    def count_pages_total(self):
        pages_total = 0
        if self.file:
            with self.file.open() as pdf_file:
                pdf = PdfReader(pdf_file)
                pages_total += len(pdf.pages)
        if self.file2:
            with self.file2.open() as pdf_file:
                pdf = PdfReader(pdf_file)
                pages_total += len(pdf.pages)
        return pages_total
    
    # Function counts the water waste. To produce 1xA4 paper we need ~5L of water = water_variable.
    # We multiply pages_total, water_variable and orderQuantity to get the result
    def count_water_waste(self):
        pages_total = 0
        water_variable=5
        water_waste=0
        if self.file:
            with self.file.open() as pdf_file:
                pdf = PdfReader(pdf_file)
                pages_total += len(pdf.pages)
                water_waste=(pages_total)*(self.orderQuantity)*(water_variable)
        if self.file2:
            with self.file2.open() as pdf_file:
                pdf = PdfReader(pdf_file)
                pages_total += len(pdf.pages)
                water_waste=(pages_total)*(self.orderQuantity)*(water_variable)
        return water_waste

# overrides save method of Order model to automatically set the orderManual field to True if file or file2 have a value, keeps False otherwise.
    def save(self, *args, **kwargs):
        if self.file or self.file2:
            self.orderManual = True
        if self.video:
            self.orderVideo = True
        else:
            self.orderManual = False
            self.orderVideo = False
        super().save(*args, **kwargs)