from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import LoginForm, RegisterForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'portfoliolab_app/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                redirect_url = request.GET.get('next', 'landing-page')
                return redirect(redirect_url)
        message_validate = "Podany login lub hasło jest nieprawidłowe !"
        return render(request, 'portfoliolab_app/login.html', {'form': form, 'message_validate': message_validate})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'portfoliolab_app/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('login')
        return render(request, 'portfoliolab_app/register.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('landing-page')
