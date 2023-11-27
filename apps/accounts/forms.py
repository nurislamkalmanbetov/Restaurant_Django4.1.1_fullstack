from django import forms




class LoginForm(forms.Form):
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput())
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput())