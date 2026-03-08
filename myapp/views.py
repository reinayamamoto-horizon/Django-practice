from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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

    if post.user != request.user:
        return redirect('post_article', pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_article', pk=post.pk)
    else:
        form = ArticleForm(instance=post)

    return render(request, 'myapp/create.html', {'form': form})

@login_required
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user 
            form.save()
            return redirect("home")  
    else:
        form = ArticleForm()

    return render(request, "myapp/create.html", {"form": form})

@login_required
def delete_article(request, pk):
    post = get_object_or_404(Article, pk=pk)
    # 投稿者本人のみ削除可能
    if post.user != request.user:
        # 権限がない場合は 403 やホームにリダイレクトなど
        return redirect('post_article', pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    # GET の場合は記事詳細に戻す（通常はフォームから POST される想定）
    return redirect('post_article', pk=pk)
