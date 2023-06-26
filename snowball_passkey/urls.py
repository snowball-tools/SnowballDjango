from django.urls import path
from . import views


app_name = "snowball_passkey"

urlpatterns = [
    path("login/begin/", views.login_begin, name="login-begin"),
    path("login/verify/", views.login_verify, name="login-verify"),
    path("register/begin/", views.register_begin, name="register-begin"),
    path("register/verify/", views.register_verify, name="register-verify"),
    path("key/rename/", views.rename_key, name="rename-key"),
    path("key/delete/", views.delete_key, name="delete-key"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
]
