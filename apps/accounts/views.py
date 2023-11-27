from django.shortcuts import render, redirect

from django.views.generic import FormView
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.http import HttpResponse

from apps.accounts.forms import LoginForm
from apps.accounts.models import User 



class LoginView(FormView):
    form_class = LoginForm
    template_name = "login.html"

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        email = data["email"]
        password = data["password"]
        user = authenticate(email=email,password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect("index")
            return HttpResponse("Ваш аккаунт не активен!")
        return HttpResponse("Введенные данные не корректны!")



            
