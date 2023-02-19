from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import adminpage, register, update, delete


urlpatterns = [ 
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name= 'logout'),
    path('adminpage/', adminpage, name='adminpage'),
    path('register/', register, name='register'),
    path('update/<int:user_id>/', update, name='update'),
    path('delete/<int:pk>',  delete, name='delete')  
]