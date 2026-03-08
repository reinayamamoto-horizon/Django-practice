from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'article_text', 'article', 'tag']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Article Title'}),
            'article_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "What's this article about?"}),
            'article': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Write your article (in markdown)'}),
            'tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tags'}),
        }
   