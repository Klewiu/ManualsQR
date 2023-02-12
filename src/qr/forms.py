from django import forms
from .models import Order
from django.core.exceptions import ValidationError

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['orderTag','orderCompany','orderName','orderQuantity','video', 'file','fileLanguage','file2','file2Language','file3','file3Language','file4','file4Language',]  
    
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

    
        
    def clean_file(self):
        file = self.cleaned_data.get('file')
    
        if file:
            if file.content_type != 'application/pdf':
                raise ValidationError("Zły format pliku. Stosuj wyłącznie pliki PDF.")
            if file.size > 1048576:
                raise ValidationError("Rozmiar pliku nie może przekraczać 1 MB.")
        return file
    


    def clean_file2(self):
        file2 = self.cleaned_data.get('file2')

        if file2:
            if file2.content_type != 'application/pdf':
                raise ValidationError("Zły format pliku. Stosuj wyłącznie pliki PDF.")
            if file2.size > 1048576:
                raise ValidationError("Rozmiar pliku nie może przekraczać 1 MB.")
        return file2

    def clean_file3(self):
        file3 = self.cleaned_data.get('file3')


        if file3:
            if file3.content_type != 'application/pdf':
                raise ValidationError("Zły format pliku. Stosuj wyłącznie pliki PDF.")
            if file3.size > 1048576:
                raise ValidationError("Rozmiar pliku nie może przekraczać 1 MB.")
        return file3

    def clean_file4(self):
        file4 = self.cleaned_data.get('file4')

        if file4:
            if file4.content_type != 'application/pdf':
                raise ValidationError("Zły format pliku. Stosuj wyłącznie pliki PDF.")
            if file4.size > 1048576:
                raise ValidationError("Rozmiar pliku nie może przekraczać 1 MB.")
        return file4
