from django.shortcuts import render, reverse
from django.views import View


class LandingPageView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/index.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/register.html')

