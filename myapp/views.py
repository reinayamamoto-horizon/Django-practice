from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article

def home(request):
    posts = Article.objects.all().order_by('-created_at')
    return render(request, 'myapp/home.html', {
        'title': 'ホーム画面',
        'posts' : posts
    })

def post_article(request, pk):
    post = get_object_or_404(Article,pk=pk)
    return render(request, 'myapp/article.html', {'post':post})

def editor_article(request, pk):
    post = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_article', pk=post.pk)
    else:
        form = ArticleForm(instance=post)

    return render(request, 'myapp/create.html', {'form': form})

def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  
    else:
        form = ArticleForm()

    return render(request, "myapp/create.html", {"form": form})
