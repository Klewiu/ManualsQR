from django.urls import path
from .views import Home, generate_qr, add_order, order_detail, client, qr_code_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('client/', client, name='client'),
    path('add/', add_order, name='add_order'),
    path('detail/<uuid:order_uuid>/', order_detail, name='order_detail'),
    path('qr/<int:order_id>.png', generate_qr, name='generate_qr'),
    path('qr_code/<uuid:order_uuid>/', qr_code_view, name='qr_code_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
