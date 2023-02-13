from django import forms
from .models import Order
from django.core.exceptions import ValidationError


class OrderForm(forms.ModelForm):
  
    # overides label names for file-loaded fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['file', 'file2', 'file3', 'file4']:
            self.fields[field].widget.clear_checkbox_label = 'Usuń'
            self.fields[field].widget.initial_text = "Aktualny Plik"
            self.fields[field].widget.input_text = "Zmień"
         

    class Meta:
        model = Order
        fields = ['orderTag','orderCompany','orderName','orderQuantity','video', 'file','fileLanguage','file2','file2Language','file3','file3Language','file4','file4Language']

         
    def clean(self):
        cleaned_data = super().clean()
    
        if cleaned_data.get('fileLanguage') and not cleaned_data.get('file'):
            raise ValidationError("Nie możesz dodać języka bez wgranego pliku")
        
        if cleaned_data.get('file2Language') and not cleaned_data.get('file2'):
            raise ValidationError("Nie możesz dodać języka bez wgranego pliku")
        
        if cleaned_data.get('file3Language') and not cleaned_data.get('file3'):
            raise ValidationError("Nie możesz dodać języka bez wgranego pliku")
        
        if cleaned_data.get('file4Language') and not cleaned_data.get('file4'):
            raise ValidationError("Nie możesz dodać języka bez wgranego pliku")

        return cleaned_data

 
        
