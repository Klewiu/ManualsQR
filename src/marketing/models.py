from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from PIL import Image

# Validators for slide height
def validate_image_height(slide):
    set_height = 300
    set_width = 1000
    try:
        with Image.open(slide) as img:
            height = img.height
            width = img.width
            if height != set_height or width != set_width:
                raise ValidationError(f"Zdjęcie musi być o wysokości {set_height} px i szerokości {set_width} px")
    except Exception:
        raise ValidationError(f"Zdjęcie musi być o wysokości {set_height} px i szerokości {set_width} px")

# Validators for slide extension. Use FileExtensionValidator as parrent to change text on PL.
class CustomFileExtensionValidator(FileExtensionValidator):
    def __init__(self, *args, **kwargs):
        self.message = "Niedozwolony typ pliku. Dozwolone są pliki w formacie: %(allowed_extensions)s."
        super().__init__(*args, **kwargs)
       

# Model class
class Marketing (models.Model):
    label = models.CharField(max_length=40, verbose_name='Tytuł slajdu')
    slide = models.FileField(upload_to='marketing',  verbose_name="Grafika slajdu",null=True, blank=True, validators=[CustomFileExtensionValidator(allowed_extensions=['png','jpg']), validate_image_height])
   
    class Meta:
        verbose_name = ("Baner Marketingowy")
        verbose_name_plural = ("Banery Marketingowe")
