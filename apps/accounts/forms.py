from django import forms




class LoginForm(forms.Form):
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={"class":"main-input-box"}))
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={"class":"main-input-box"}))

