from django.shortcuts import render
from .forms import MarketingForm
from .models import Marketing
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView, DeleteView
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.urls import reverse_lazy
from qr.views import SuperuserRequiredMixin


# Create your views here.

class MarketingList(SuperuserRequiredMixin, ListView):
    model = Marketing
    template_name = "marketing/marketing.html"

class MarketingCreate(SuperuserRequiredMixin, CreateView):
    model = Marketing
    fields = '__all__'
    template_name='marketing/create_Ad.html'
    success_url = reverse_lazy('marketing:marketing-list')

@receiver(pre_delete, sender=Marketing)
def my_callback(sender, instance, **kwargs):
    instance.slide.delete()


class MarketingDelete(SuperuserRequiredMixin, DeleteView):
    model = Marketing
    template_name = 'marketing/marketing_confirm_delete.html'
    success_url = reverse_lazy('marketing:marketing-list')
