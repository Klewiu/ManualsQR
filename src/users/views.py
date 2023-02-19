from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def adminpage(request):
    users = User.objects.all()
    context = {
        
        "title": "Admin Page",
        "users": users,
        
    }
    return render(request, "users/adminpage.html", context)


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


def delete_user (request, pk):
    User.objects.filter(id=pk).delete()
    users = User.objects.all()
    return render (request, 'users/partials/user-list.html', {'users':users})