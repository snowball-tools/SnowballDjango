from django.urls import path
from . import views

app_name = "snowball_main"

urlpatterns = [
    path("", views.Home, name="home"),
    path(
        ".well-known/apple-app-site-association",
        views.apple_app_site_association,
        name="apple-app-site-association",
    ),
    path("login/", views.login, name="login"),
]
