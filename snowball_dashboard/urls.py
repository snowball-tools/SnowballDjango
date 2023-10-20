from django.urls import path
from .views import index

app_name = "snowball_dashboard"

urlpatterns = [
    path("", index, name="index"),
]