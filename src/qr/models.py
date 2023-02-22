from django.db import models
from django.contrib.auth.models import User
import uuid
from PyPDF2 import PdfReader
from .validators import validate_file_size, validate_pdf


# Create your models here.
class Order (models.Model):

    STATUS_CHOICES = (('Zlecone', 'Zlecone'),('Podjęte', 'Podjęte'),('Zakończone', 'Zakończone'),)

    
    orderTag= models.CharField(max_length=18, verbose_name='WZP', unique=True)
    orderCompany = models.CharField(max_length=40, verbose_name='Firma')
    orderName = models.CharField(max_length=40, verbose_name='Produkt')
    orderQuantity = models.IntegerField(verbose_name='Ilość')
    orderDate = models.DateTimeField(auto_now=True, verbose_name='Data Utworzenia')
    orderManager = models.ForeignKey(User, on_delete= models.SET_DEFAULT, verbose_name='Autor Zlecenia', default=1)
    orderManual = models.BooleanField(default=False)
    orderVideo = models.BooleanField(default=False)
    orderStatus = models.CharField(max_length=20, choices=STATUS_CHOICES)
    file = models.FileField(upload_to='manual/', null=True, blank=True, verbose_name="Instrukcja I", validators=[validate_file_size, validate_pdf])
    fileLanguage = models.CharField(max_length=20, verbose_name ='Język instrukcji I', null=True, blank=True)
    file2 = models.FileField(upload_to='manual/', null=True, blank=True, verbose_name="Instrukcja II", validators=[validate_file_size, validate_pdf])
    file2Language = models.CharField(max_length=20, verbose_name ='Język instrukcji II', null=True, blank=True)
    file3 = models.FileField(upload_to='manual/', null=True, blank=True, verbose_name="Instrukcja III", validators=[validate_file_size, validate_pdf])
    file3Language = models.CharField(max_length=20, verbose_name ='Język instrukcji III', null=True, blank=True)
    file4 = models.FileField(upload_to='manual/', null=True, blank=True, verbose_name="Instrukcja IV", validators=[validate_file_size, validate_pdf])
    file4Language = models.CharField(max_length=20, verbose_name ='Język instrukcji IV', null=True, blank=True)
    url = models.UUIDField(default=uuid.uuid4, editable=False)
    video = models.TextField(max_length=10000, verbose_name='Multimedia/Video Embed', blank=True, null=True)
    
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

    def count_pages_file3(self):
        pages3 = 0
        if self.file3:
            with self.file3.open() as pdf_file:
                pdf = PdfReader(pdf_file)
                pages3 += len(pdf.pages)
        return pages3

    def count_pages_file4(self):
        pages4 = 0
        if self.file4:
            with self.file4.open() as pdf_file:
                pdf = PdfReader(pdf_file)
                pages4 += len(pdf.pages)
        return pages4    

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
        if self.file3:
            with self.file3.open() as pdf_file:
                pdf = PdfReader(pdf_file)
                pages_total += len(pdf.pages)
        if self.file4:
            with self.file4.open() as pdf_file:
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
        if self.file3:
            with self.file3.open() as pdf_file:
                pdf = PdfReader(pdf_file)
                pages_total += len(pdf.pages)
                water_waste=(pages_total)*(self.orderQuantity)*(water_variable)
        if self.file4:
            with self.file4.open() as pdf_file:
                pdf = PdfReader(pdf_file)
                pages_total += len(pdf.pages)
                water_waste=(pages_total)*(self.orderQuantity)*(water_variable)
        return water_waste

# overrides save method of Order model to automatically set the orderManual field to True if file or file2 have a value, keeps False otherwise.
    def save(self, *args, **kwargs):
        self.orderManual = bool(self.file or self.file2 or self.file3 or self.file4)
        self.orderVideo = bool(self.video)
        super().save(*args, **kwargs)


