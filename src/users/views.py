from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.



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


def delete (request, pk):
    User.objects.filter(id=pk).delete()
    users = User.objects.all()
    return render (request, 'users/partials/user-list.html', {'users':users})

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