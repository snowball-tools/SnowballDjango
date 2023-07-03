from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="{% url 'login' %}")
def profile(request):
    return render(request, "profile.html")


@login_required(login_url="{% url 'login' %}")
def passkeys(request):
    if request.method == "POST":
        # to do
        pass
    return render(request, "passkeys.html")
