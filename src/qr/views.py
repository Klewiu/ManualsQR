from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Order
import qrcode
from django.http import HttpResponse
from .forms import OrderForm
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy


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
    num_pages = order.count_pages()
    water_variable = 5
    water_waste = int(num_pages)*int(order.orderQuantity)*(water_variable)
    return render(request, 'qr/order_detail.html', {'order': order, 'pages':num_pages, 'water':water_waste, 'qr_url': generate_qr(request, order.id)})

def qr_code_view(request, order_uuid):
    order = Order.objects.get(url=order_uuid)
    return render(request, 'qr/qr_code.html', {'order': order})

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'qr/order_confirm_delete.html'
    success_url = reverse_lazy('home')

def client(request):
    context = {'title': 'Client panel'}
    return render(request, 'qr/client.html', context)