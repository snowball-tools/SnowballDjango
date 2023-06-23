from django.urls import path
from . import views

app_name = "snowball_passkey"

urlpatterns = [
    path("begin_registration/", views.begin_registration, name="begin_registration"),
    path("finish_registration/", views.finish_registration, name="finish_registration"),
    path(
        "begin_authentication/", views.begin_authentication, name="begin_authentication"
    ),
    path(
        "finish_authentication/",
        views.finish_authentication,
        name="finish_authentication",
    ),
]
