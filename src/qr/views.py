from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Order
from marketing.models import Marketing
from notifications.models import Notifications
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
from django.contrib import messages
from django.core.mail import send_mail


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
    notifications= Notifications.objects.all()
    email_list = [notification.email for notification in notifications]
    print(email_list)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.orderManager = request.user
            order.save()
            messages.success(request, "Dodano Zlecenie!")
            
            # sendgin email to user add in notifications app
            send_mail(
            f"W Assemble QR dodano nowe zlecenie - {order.orderTag} !",
            f' Zlecenie o numerze "{order.orderTag}" i nazwie "{order.orderName}", oczekuje na przygotowanie i dodanie instrukcji.',
            "assembleqr@gmail.com",
            email_list , fail_silently=True,
            )

            return redirect('order_detail', order_uuid=order.url)
        else:
            # clears fileLanguage fields on error
            form = OrderForm(request.POST.copy())
            for key in ['fileLanguage', 'file2Language', 'file3Language', 'file4Language']:form.data[key] = ''
            messages.error(request, "Coś poszło nie tak! Pole języka musi być puste, jeśli nie wgrywasz pliku. Właściwy format to PDF do 1 MB. ")
    else:
        form = OrderForm()
    return render(request, 'qr/add_order.html', {'form': form})

def update_order(request, order_uuid):
    order = Order.objects.get(url=order_uuid)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            order = form.save()
            messages.success(request, "Zaktualizowano Zlecenie!")
            return redirect('order_detail', order_uuid=order.url)
        else:
            messages.error(request, "Coś poszło nie tak! Pole języka musi być puste, jeśli nie wgrywasz pliku. Właściwy format to PDF do 1 MB. ")
    else:
        form = OrderForm(instance=order)
    return render(request, 'qr/update_order.html', {'form': form})




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

    if order.file3:
        num_pages3 = order.count_pages_file3()
        water_variable = 5
        water_waste3 = int(num_pages3)*int(order.orderQuantity)*(water_variable)
    else:
        num_pages3 = None
        water_waste3 = None
    
    if order.file4:
        num_pages4 = order.count_pages_file4()
        water_variable = 5
        water_waste4 = int(num_pages4)*int(order.orderQuantity)*(water_variable)
    else:
        num_pages4 = None
        water_waste4 = None

    context={
        'order': order,
        'pages1':num_pages1,
        'pages2':num_pages2,
        'pages3':num_pages3,
        'pages4':num_pages3,
        'water1':water_waste1,
        'water2':water_waste2,
        'water3':water_waste3,
        'water4':water_waste4,
        'qr_url':generate_qr(request, order.id)
    }

    return render(request, 'qr/order_detail.html',  context)

def qr_print(request, order_uuid):
    order = Order.objects.get(url=order_uuid)

    context = {
        'order': order,
        'orderCompany': order.orderCompany,
        'orderName': order.orderName,
    }
    return render(request, 'qr/qr_print.html', context)


def qr_code_view(request, order_uuid):
    total_water_waste=0
    order_qs_water = Order.objects.all()
    for obj in order_qs_water:
        total_water_waste+=obj.count_water_waste()
    order = Order.objects.get(url=order_uuid)
    marketing = Marketing.objects.all()
    context={
        'order': order,
        'marketing':marketing,
        'total_water_waste':total_water_waste
    }
    return render(request, 'qr/qr_code.html', context)




# as OrderDeleteView class does not exacute custom logic, so a pre_delete signal completes file deletion
@receiver(pre_delete, sender=Order)
def my_callback(sender, instance, **kwargs):
    instance.file.delete()
    instance.file2.delete()
    instance.file3.delete()
    instance.file4.delete()

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



