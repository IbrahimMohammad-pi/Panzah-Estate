from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    return render(request, "main/index.html")


def login_page(request):
    return render(request, "main/login.html")


def register_page(request):
    return render(request, "main/register.html")


def landlord_home_page(request):
    return render(request, "main/landlord_home.html")


def tenant_home(request):
    # tenant = get_object_or_404(Tenant, id=1)
    return render(request, "main/tenant_home.html")


def user_profile_page(request):
    return render(request, "main/user_profile.html")


def analytics_page(request):
    return render(request, "main/analytics.html")
