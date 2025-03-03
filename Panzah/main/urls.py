from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_page, name="login_page"),
    path("register/", views.register_page, name="register_page"),
    path("landlord_home/", views.landlord_home_page, name="landlord_home"),
    path("tenant_home/", views.tenant_home, name="tenant_home"),
    path("analytics/", views.analytics_page, name="analytics_page"),
    path("user_profile/", views.user_profile_page, name="user_profile_page"),
]
