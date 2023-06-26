import os
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.defaults import server_error as django_server_error
from .models import Window
from django import forms


def Home(request):
    # overengineered this and backtracking. can source from database (for funsies)
    links = [
        Window(
            name="SnowballSwiftKit",
            url="https://github.com/snowball-tools/SnowballSwiftKit",
            elementId="snowballswiftkit",
        ),
        Window(
            name="This Django App",
            url="https://github.com/snowball-tools/SnowballDjango",
            elementId="thisdjangoapp",
        ),
        Window(
            name="Convert SVG files to SF Symbol",
            url="https://github.com/snowball-tools/ConvertSVGToSFSymbol",
            elementId="convertsvgfilestosfsymbol",
        ),
        Window(
            name="Example Typescript React Native Expo App",
            url="https://github.com/snowball-tools/SnowballExampleTypescriptExpo",
            elementId="exampletypescriptreactnativeexpoapp",
        ),
    ]

    return render(request, "home.html", {"links": links})


class SnowballPasskey(forms.Form):
    name = forms.CharField(max_length=100)


def login(request):
    form = SnowballPasskey(request.POST or None)

    if form.is_valid():
        # redirect to a new URL: /passkey/login/begin/
        return redirect("snowball_passkey:login-begin")

    return render(request, "login.html", {"form": form})


# error views
def error_view(request, exception=None, error_code=None):
    return render(
        request, "error.html", {"window": Window(name=exception, title=error_code)}
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


# https://developer.apple.com/documentation/xcode/supporting-associated-domains
def apple_app_site_association(request):
    data = {
        "applinks": {
            "details": [
                {
                    "appIDs": ["9SAQ42S589.xyz.snowballtools.example"],
                    "components": [],
                }
            ]
        },
        "webcredentials": {"apps": ["9SAQ42S589.xyz.snowballtools.example"]},
        "appclips": {
            "apps": [
                "xyz.snowballtools.example.Clips",
            ]
        },
    }
    return JsonResponse(data)
