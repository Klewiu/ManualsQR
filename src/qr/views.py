from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Order
import qrcode
from django.http import HttpResponse
from .forms import OrderForm
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Sum, F


class Home(ListView):
    model=Order
    template_name = "qr/home.html"
    ordering = ["-orderDate"]
    
    # get context data to add new context
    def get_context_data(self, **kwargs):
        total_water_waste=0
        # get all Order frome Home and store it in queryset
        queryset = super().get_queryset()
        # call model method count_water_waste() on each queryset object -> obj and += result, to total_water_waste variable
        for obj in queryset:
            total_water_waste+=obj.count_water_waste()
        # get context frome Home and then create new context field.
        # finnaly return context
        context = super(Home, self).get_context_data(**kwargs)
        context["total_water_waste"] = total_water_waste
        return context
    

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
            if not form.cleaned_data['file']:
                order.file = None
            if not form.cleaned_data['file2']:
                order.file2 = None
            order.orderManager = request.user
            order.save()
            return redirect('order_detail', order_uuid=order.url)
    else:
        form = OrderForm()
    return render(request, 'qr/add_order.html', {'form': form})

def order_detail(request, order_uuid):
    order = Order.objects.get(url=order_uuid)
    if order.file or order.file2:
        num_pages = order.count_pages_total()
        water_variable = 5
        water_waste = int(num_pages)*int(order.orderQuantity)*(water_variable)
    else:
        num_pages = None
        water_waste = None
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