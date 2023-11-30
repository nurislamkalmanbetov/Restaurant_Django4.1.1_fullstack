from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.accounts.models import User



class LoginForm(forms.Form):
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={"class":"main-input-box"}))
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={"class":"main-input-box"}))



class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form-control"})
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            ]
