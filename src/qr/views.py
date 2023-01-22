from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Order
import qrcode
from django.http import HttpResponse
from .forms import OrderForm
from django.views.generic import ListView

class Home(ListView):
    model=Order
    template_name = "qr/home.html"
    ordering = ["-orderDate"]

def generate_qr(request, order_id):
    order = Order.objects.get(id=order_id)
    url = request.build_absolute_uri(reverse('qr_code_view', args=[order.url]))
    img = qrcode.make(url)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.orderManager = request.user
            order.save()
            return redirect('order_detail', order_uuid=order.url)
    else:
        form = OrderForm()
    return render(request, 'qr/add_order.html', {'form': form})

def order_detail(request, order_uuid):
    order = Order.objects.get(url=order_uuid)
    return render(request, 'qr/order_detail.html', {'order': order, 'qr_url': generate_qr(request, order.id)})

def qr_code_view(request, order_uuid):
    order = Order.objects.get(url=order_uuid)
    return render(request, 'qr/qr_code.html', {'order': order})

def client(request):
    context = {'title': 'Client panel'}
    return render(request, 'qr/client.html', context)