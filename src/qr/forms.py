from django import forms
from .models import Order, Marketing

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['orderTag','orderCompany','orderName','orderQuantity','file','fileLanguage','file2','file2Language','video']


class MarketingForm(forms.ModelForm):
    class Meta:
        model = Marketing
        fields = '__all__'