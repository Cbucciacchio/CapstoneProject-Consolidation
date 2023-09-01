from django.shortcuts import render

def home_view(request):
    return render(request, "home/homepage.html")

def default(request):
    return render(request, "home/homepage.html")