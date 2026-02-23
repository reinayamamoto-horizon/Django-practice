from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html', {
        'title': 'ホーム画面'
    })