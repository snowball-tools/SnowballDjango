from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
import requests


@login_required(login_url="{% url 'login' %}")
def profile(request):
    return render(request, "profile.html")


def loginView(request):
    context = {}
    if request.method == "POST":
        print("post")
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user:
            login(request, user)
            print("logged in user")
            return HttpResponseRedirect(reverse("home"))
        context["invalid"] = True
    return render(request, "login.html", context)
