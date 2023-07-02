from django.urls import include, path
from . import views

app_name = "snowball_authentication"

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("passkeys/", views.passkeys, name="passkeys"),
]
