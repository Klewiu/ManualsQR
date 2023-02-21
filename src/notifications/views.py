from django.shortcuts import render
from notifications.models import Notifications
from django.views.generic import ListView
from django.contrib.auth.decorators import user_passes_test
from qr.views import SuperuserRequiredMixin


# Create your views here.

class NotificationsList(SuperuserRequiredMixin, ListView):
    model = Notifications
    template_name = 'notifications/notifications.html'
    # to chagne in template objects_list to notifications
    context_object_name = 'notifications'
     
def add_notification(request):
    err_message=[]
    # in get we enter atribute from notifications.html <input name = "this atrribiute" ...
    email = request.POST.get('email')

    # create in db when not uniqe - add error and pass to context
    notification, created = Notifications.objects.get_or_create(email=email)
    if not created:
        err_message = f"Sprawdź czy adres mailowy {email} nie występuje już na liście"
    
    #return qs for displaying in template
    notifications = Notifications.objects.all()

    context = {
        'notifications':notifications,
        'err_message': err_message,
    }

    return render (request, 'notifications/partials/notifications-list.html', context)

@user_passes_test(lambda u: u.is_authenticated and u.is_superuser)
def delete_notification(request, pk):
    Notifications.objects.filter(id=pk).delete()
    notifications = Notifications.objects.all()
    return render (request, 'notifications/partials/notifications-list.html', {'notifications':notifications})