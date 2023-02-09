from django.shortcuts import render
from notifications.models import Notifications
from django.views.generic import ListView



# Create your views here.

class NotificationsList(ListView):
    model = Notifications
    template_name = 'notifications/notifications.html'
    # to chagne in template objects_list to notifications
    context_object_name = 'notifications'
     
def add_notification(request):
    err_message=[]
    # in get we enter atribute fron notifications.html <input name = "this atrribiute" 
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
