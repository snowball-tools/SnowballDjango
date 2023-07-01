from django.urls import path
from . import views

app_name = "snowball_authentication"

urlpatterns = [
    path("applelogin", views.AppleLogin, name="applelogin"),
]
