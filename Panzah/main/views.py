from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def login_page(request):
    return render(request, 'main/login.html')

def register_page(request):
    return render(request, 'main/register.html')

def landlord_home_page(request):
    return render(request, 'main/LL_home.html')

def tenant_home(request):
    return render(request, 'main/ten_home.html')

def user_profile_page(request):
    return render(request, 'main/user_profile.html')

def analytics_page(request):
    return render(request, 'main/analytics.html')
