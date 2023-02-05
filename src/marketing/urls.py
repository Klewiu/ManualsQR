from django.urls import path
from .views import marketing
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [  
    path('marketing/', marketing, name='marketing')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)