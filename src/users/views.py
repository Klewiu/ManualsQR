from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import PasswordResetView

# Create your views here.

@user_passes_test(lambda u: u.is_authenticated and u.is_superuser)
def adminpage(request):
    users = User.objects.all()
    context = {
        
        "title": "Admin Page",
        "users": users,
        
    }
    return render(request, "users/adminpage.html", context)

@user_passes_test(lambda u: u.is_authenticated and u.is_superuser)
def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Utworzono nowego użytkownika {username}!')
            return redirect('adminpage')
    else:
        form = UserRegisterForm()
    return render (request, "users/register.html", {'form': form})

@user_passes_test(lambda u: u.is_authenticated and u.is_superuser)
def delete (request, pk):

    user = get_object_or_404(User, id=pk)
    user.is_active = False
    user.save()
    users = User.objects.all()
    return render (request, 'users/partials/user-list.html', {'users':users})

@user_passes_test(lambda u: u.is_authenticated and u.is_superuser)
def restore (request, pk):

    user = get_object_or_404(User, id=pk)
    user.is_active = True
    user.save()
    users = User.objects.all()
    return render (request, 'users/partials/user-list.html', {'users':users})

    
@user_passes_test(lambda u: u.is_authenticated and u.is_superuser)
def update(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Zaktualizowano Użytkownika!')
            return redirect('adminpage')
    else:
        form = UserUpdateForm(instance=user)

    context = {
        'form': form,
        'user_id': user_id
    }

    return render(request, 'users/update.html', context)

class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        # Check if the email entered by the user exists in the database
        email = form.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            messages.error(self.request, 'Użytkownik o tym adresie email nie istnieje.')
            return self.form_invalid(form)

        # Call the parent class's form_valid() method to send the password reset email
        return super().form_valid(form)