from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.db.models import Sum, Count

from portfoliolab_app.models import Donation, Institution, Account


class LandingPageView(View):
    def get(self, request):
        institutions_choice_fund = Institution.objects.filter(type='fundacja')
        institutions_choice_org = Institution.objects.filter(type='organizacja pozarządowa')
        institutions_choice_zbi = Institution.objects.filter(type='zbiórka lokalna')
        sum_bags = Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
        institutions_supported = Donation.objects.aggregate(Count('institution'))['institution__count']
        return render(request, 'portfoliolab_app/index.html',
                      {'institutions_choice_fund': institutions_choice_fund,
                       'institutions_choice_org': institutions_choice_org,
                       'institutions_choice_zbi': institutions_choice_zbi,
                       'sum_bags': sum_bags, 'institutions_supported': institutions_supported})


class AddDonationView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('landing-page')
        if user not in Account.objects.all():
            message = """
            Wygląda na to, że nie masz u nas konta. 
            Zarejetruj sie i spróbuj ponownie.
            """
            return render(request, 'portfoliolab_app/register.html', {'message': message})
        # message = "Podany login lub hasło jest nieprawidłowe."
        # return render(request, 'portfoliolab_app/login.html', {'message': message})


class RegisterView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/register.html')

    def post(self, request):
        first_name = request.POST.get('name')
        last_name = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password = request.POST.get('password2')
        user = Account.objects.create_user(first_name=first_name, last_name=last_name,
                                           email=email, password=password)
        return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('landing-page')
