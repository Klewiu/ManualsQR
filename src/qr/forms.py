from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['orderTag','orderCompany','orderName','orderQuantity','orderVideo','file', 'file2']
