from django.shortcuts import render
from django.http import JsonResponse
from django.views.defaults import server_error as django_server_error
from .models import Window


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


def contact(request):
    return render(
        request,
        "generic_window.html",
        {
            "window": Window(
                title="contact",
                style="style='width: 80%; top: 10%; left: 10%; height: 80%;'",
                contents="<p>viv@snowballtools.xyz</p>",
            )
        },
    )


# error views
def error_view(request, exception=None, error_code=None):
    # to do fix exception handling
    return render(
        request,
        "generic_window.html",
        {
            "window": Window(
                name=exception,
                title=error_code,
                style="style='width: 80%; top: 10%; left: 10%; height: 80%;'",
                contents="<p>error</p>",
            )
        },
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
                    "appIDs": [
                        "9SAQ42S589.xyz.snowballtools.example, 9SAQ42S589.xyz.snowballtools.app"
                    ],
                    "components": [],
                }
            ]
        },
        "webcredentials": {
            "apps": [
                "9SAQ42S589.xyz.snowballtools.example, 9SAQ42S589.xyz.snowballtools.app"
            ]
        },
        "appclips": {
            "apps": [
                "xyz.snowballtools.example.Clips",
            ]
        },
    }
    return JsonResponse(data)
