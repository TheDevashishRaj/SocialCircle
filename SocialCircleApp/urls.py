from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Index"),
    path("settings", views.settings, name="Settings"),
    path("upload", views.upload, name="Upload"),
    path("signup", views.signup, name="SignUp"),
    path("signin", views.signin, name="Signin"),
    path("logout", views.logout, name="Logout"),
]