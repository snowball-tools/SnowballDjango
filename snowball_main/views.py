from django.shortcuts import render
from django.views.defaults import (
    server_error as django_server_error,
    page_not_found as django_page_not_found,
)


def home(request):
    return render(request, "snowball_main/home.html")


def error_view(request, exception=None, error_code=None):
    return render(
        request,
        "snowball_main/error.html",
        {"error_code": error_code, "exception": exception},
    )


def server_error(request, *args, **kwargs):
    return error_view(
        request, error_code=500, exception=django_server_error(request, *args, **kwargs)
    )


def page_not_found(request, exception, *args, **kwargs):
    return error_view(request, error_code=404, exception=exception)


def permission_denied(request, exception, *args, **kwargs):
    return error_view(request, error_code=403, exception=exception)


def bad_request(request, exception, *args, **kwargs):
    return error_view(request, error_code=400, exception=exception)
