from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')) 
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user'))

def show_user(request):
    return render(request, 'authentication/user.html', {
        "username": request.user.username
    })


def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return HttpResponseRedirect(reverse('user_auth:register'))

        # Create the new user
        user = User.objects.create_user(username=username, password=password, first_name=first_name)
        messages.success(request, "Registration successful! Please login.")
        return HttpResponseRedirect(reverse('user_auth:login'))

    return render(request, 'authentication/register.html')
