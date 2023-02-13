import os
from django.core.exceptions import ValidationError




def validate_file_size(value):
    filesize= value.size
    if filesize > 1 * 1024 * 1024:
        raise ValidationError("Plik nie może być większy niż 1 MB")
    else:
        return value

def validate_pdf(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError("Plik musi mieć format PDF")
    else:
        return value