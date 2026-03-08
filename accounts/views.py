from django.shortcuts import render, redirect
from .models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm

def signup_view (request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            login(request,user)
        except IntegrityError:
            return render(request, "accounts/signup.html", {"error": "このメールアドレスは既に登録されています"})

        return redirect("home")

    return render(request, "accounts/signup.html")


def login_view(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "accounts/login.html", {"error": "ログイン失敗"})

    return render(request, "accounts/login.html")


@login_required 
def settings(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = UserForm(instance=request.user)

    return render(request, 'accounts/settings.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("login")