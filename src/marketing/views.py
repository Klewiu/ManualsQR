from django.shortcuts import render
from .forms import MarketingForm
from .models import Marketing
from django.shortcuts import render, redirect

# Create your views here.

def marketing(request):
    context = {'title': 'Marketing panel'}
    return render(request, 'marketing/marketing.html', context)
