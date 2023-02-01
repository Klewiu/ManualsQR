from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Order
import qrcode
from django.http import HttpResponse
from .forms import OrderForm
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Sum, F
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Home(ListView):
    model=Order
    template_name = "qr/home.html"
    ordering = ["-orderDate"]
    paginate_by = 8 # Number of items to display per page
    
    def get_context_data(self, **kwargs):
        total_water_waste=0
        queryset = super().get_queryset()
        for obj in queryset:
            total_water_waste+=obj.count_water_waste()
        
        context = super(Home, self).get_context_data(**kwargs)
        context["total_water_waste"] = total_water_waste
        
        # Paginate the queryset
        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        
        # Add the paginated queryset to the context
        context['object_list'] = queryset
        
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
            if not form.cleaned_data['video']:
                order.video = None
            order.orderManager = request.user
            order.save()
            return redirect('order_detail', order_uuid=order.url)
    else:
        form = OrderForm()
    return render(request, 'qr/add_order.html', {'form': form})

def order_detail(request, order_uuid):
    order = Order.objects.get(url=order_uuid)
    if order.file:
        num_pages1 = order.count_pages_file1()
        water_variable = 5
        water_waste1 = int(num_pages1)*int(order.orderQuantity)*(water_variable)
    else:
        num_pages1 = None
        water_waste1 = None
    if order.file2:
        num_pages2 = order.count_pages_file2()
        water_variable = 5
        water_waste2 = int(num_pages2)*int(order.orderQuantity)*(water_variable)
    else:
        num_pages2 = None
        water_waste2 = None

    context={
        'order': order,
        'pages1':num_pages1,
        'pages2':num_pages2,
        'water1':water_waste1,
        'water2':water_waste2,
        'qr_url':generate_qr(request, order.id)
    }

    return render(request, 'qr/order_detail.html',  context)

def qr_code_view(request, order_uuid):
    order = Order.objects.get(url=order_uuid)
    return render(request, 'qr/qr_code.html', {'order': order})


# as OrderDeleteView class does not exacute custom logic, so a pre_delete signal completes file deletion
@receiver(pre_delete, sender=Order)
def my_callback(sender, instance, **kwargs):
    instance.file.delete()
    instance.file2.delete()

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'qr/order_confirm_delete.html'
    success_url = reverse_lazy('home')

def search(request):
    search_query = request.POST.get("search_query")
    if search_query:
        object_list = Order.objects.filter(Q(orderName__icontains=search_query) | 
                                        Q(orderTag__icontains=search_query) | 
                                        Q(orderCompany__icontains=search_query) |
                                        Q(orderManager__username__icontains=search_query))
    else:
        object_list = Order.objects.all().order_by('-orderDate')
    return render(request, "qr/object_list.html", {"object_list": object_list})
    

def client(request):
    context = {'title': 'Client panel'}
    return render(request, 'qr/client.html', context)