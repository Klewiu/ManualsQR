from django.urls import path
from .views import NotificationsList, add_notification
from django.conf import settings
from django.conf.urls.static import static

app_name = 'notifications'

urlpatterns = [  
    path('notifications/', NotificationsList.as_view(), name='notifications'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

htmx_urlpatterns = [
    path('add-notification/',  add_notification, name='add-notification') 
]

urlpatterns += htmx_urlpatterns