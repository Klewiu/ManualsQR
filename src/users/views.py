from django.shortcuts import render

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