from django.urls import path
from .views import MarketingList, MarketingCreate, MarketingDelete
from django.conf import settings
from django.conf.urls.static import static

app_name = 'marketing'

urlpatterns = [  
    path('marketing/', MarketingList.as_view(), name='marketing-list'),
    path('marketing/create', MarketingCreate.as_view(), name='marketing-create'),
    path('marketing/<int:pk>/delete/', MarketingDelete.as_view(), name='marketing-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)