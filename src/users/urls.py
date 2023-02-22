from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import adminpage, register, update, delete, CustomPasswordResetView
from django.contrib.auth import views as auth_views


urlpatterns = [ 
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name= 'logout'),
    path('adminpage/', adminpage, name='adminpage'),
    path('register/', register, name='register'),
    path('update/<int:user_id>/', update, name='update'),
    path('delete/<int:pk>',  delete, name='delete'),
    path('password-reset/', CustomPasswordResetView.as_view(template_name = 'users/password_reset.html'), name= 'password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name= 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name= 'password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name= 'password_reset_complete'),  
]