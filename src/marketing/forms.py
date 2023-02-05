from django import forms
from .models import Marketing

class MarketingForm(forms.ModelForm):
    class Meta:
        model = Marketing
        fields = '__all__'