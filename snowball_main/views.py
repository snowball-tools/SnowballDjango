from django.shortcuts import render
from django.http import JsonResponse
from django.views.defaults import server_error as django_server_error


def home(request):
    linkModels = [
        LinkModel(
            name="SnowballSwiftKit",
            url="https://github.com/snowball-tools/SnowballSwiftKit",
        ),
        LinkModel(
            name="This Django App",
            url="https://github.com/snowball-tools/SnowballDjango",
        ),
        LinkModel(
            name="Convert SVG files to SF Symbol",
            url="https://github.com/snowball-tools/ConvertSVGToSFSymbol",
        ),
        LinkModel(
            name="Example Typescript React Native Expo App",
            url="https://github.com/snowball-tools/SnowballExampleTypescriptExpo",
        ),
    ]
    return render(request, "home.html", {"links": linkModels})


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


class LinkModel:
    name = ""
    url = ""
    id = ""
    title = ""

    def __init__(self, name, url, title=""):
        self.name = name
        self.url = url
        self.id = name.lower().replace(" ", "")
        self.title = title
