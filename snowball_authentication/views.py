from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="{% url 'login' %}")
def profile(request):
    return render(request, "profile.html")


@login_required(login_url="{% url 'login' %}")
def passkeys(request):
    return render(request, "passkeys.html")
