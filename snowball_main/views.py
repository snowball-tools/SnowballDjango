from django.shortcuts import render
from django.http import JsonResponse
from django.views.defaults import server_error as django_server_error


def home(request):
    return render(request, "home.html")


# https://developer.apple.com/documentation/xcode/supporting-associated-domains
def apple_app_site_association(request):
    data = {
        "applinks": {
            "details": [
                {
                    "appIDs": [
                        "xyz.snowballtools.example",
                    ],
                    "components": [],
                }
            ]
        },
        "webcredentials": {"apps": ["xyz.snowballtools.example"]},
        "appclips": {
            "apps": [
                "xyz.snowballtools.example.Clips",
            ]
        },
    }
    return JsonResponse(data)


# error views
def error_view(request, exception=None, error_code=None):
    return render(
        request,
        "error.html",
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
