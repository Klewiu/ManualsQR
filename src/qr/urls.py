from django.urls import path
from .views import Home, generate_qr, add_order, order_detail, qr_code_view, OrderDeleteView, search, update_order, qr_print, download_file
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', Home.as_view(), name='home'),
    path("page/<int:page>/", Home.as_view(), name="home_paginated"),
    path('add/', add_order, name='add_order'),
    path('detail/<uuid:order_uuid>/', order_detail, name='order_detail'),
    path('qr/<int:order_id>.png', generate_qr, name='generate_qr'),
    path('qr_code/<uuid:order_uuid>/', qr_code_view, name='qr_code_view'),
    path('qr/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
    path('search/', search, name='search'),
    path('order/<str:order_uuid>/update/', update_order, name='update_order'),
    path('qr/<str:order_uuid>/print/', qr_print, name='qr_print'),
    path('download/<path:file_name>/', download_file, name='download_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
