from django.shortcuts import render, redirect
from .forms import UserForm

def home(request):
    return render(request, 'myapp/home.html', {
        'title': 'ホーム画面'
    })

def create(request):
    return render(request,'myapp/create.html',{
        'title': 'New Article'
    })

def create_user(request):
   if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  
    else:
        form = UserForm()

    return render(request, "myapp/create.html", {"form": form})