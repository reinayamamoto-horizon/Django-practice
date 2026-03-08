from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'profile_image']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ユーザー名'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }