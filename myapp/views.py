from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

def home(request):
    posts = Article.objects.all().order_by('-created_at')
    return render(request, 'myapp/home.html', {
        'title': 'ホーム画面',
        'posts' : posts
    })

def editor(request):
    return render(request,'myapp/editor.html',)

def create(request):
    form = ArticleForm()
    return render(request, 'myapp/create.html', {'form': form})


def create_user(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  
    else:
        form = ArticleForm()

    return render(request, "myapp/create.html", {"form": form})