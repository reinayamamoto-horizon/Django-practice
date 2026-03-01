from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="メールアドレス")
    password = forms.CharField(widget=forms.PasswordInput, label="パスワード")