from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .models import User
from .forms import LoginForm

# ログインビュー
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                if check_password(password, user.password):
                    # ログイン成功: セッションにユーザーIDを保存
                    request.session['user_id'] = user.user_id
                    return redirect('home')
                else:
                    messages.error(request, "パスワードが違います")
            except User.DoesNotExist:
                messages.error(request, "ユーザーが存在しません")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# ログアウトビュー
def logout_view(request):
    request.session.flush()  # セッション情報を削除
    return redirect('login')
