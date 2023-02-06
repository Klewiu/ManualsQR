from django.shortcuts import render
from .forms import MarketingForm
from .models import Marketing
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class MarketingList(ListView):
    model = Marketing
    template_name = "marketing/marketing.html"

class MarketingCreate(CreateView):
    model = Marketing
    fields = '__all__'
    template_name='marketing/create_Ad.html'
    success_url = reverse_lazy('marketing:marketing-list')
