from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def home(request):
    return render(request, "snowball_main/home.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            # Return an 'invalid login' error message.
            return render(
                request,
                "snowball_main/login.html",
                {"error": "Invalid username or password"},
            )
    else:
        return render(request, "snowball_main/login.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
