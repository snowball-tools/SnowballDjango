from django.shortcuts import render


def home(request):
    return render(request, "snowball_main/home.html")
