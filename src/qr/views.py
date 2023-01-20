from django.shortcuts import render
from .models import Order

# Create your views here.
def home(request):
    orders = Order.objects.all()
    context = {
      'orders': orders,
      'title': 'Strona Główna'
      }
      
    return render (request,'qr/home.html', context )

def client(request):
    context = {
      'title': 'Client panel'
      }
      
    return render (request,'qr/client.html', context )