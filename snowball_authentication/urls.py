from django.urls import include, path
from . import views

app_name = "snowball_authentication"

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("login/", views.loginView, name="login"),
]
