from django.shortcuts import render, reverse
from django.views import View
from django.db.models import Sum, Count

from portfoliolab_app.models import Donation, Institution


class LandingPageView(View):
    def get(self, request):
        institutions_choice_fund = Institution.objects.filter(type='fundacja')
        institutions_choice_org = Institution.objects.filter(type='organizacja pozarządowa')
        institutions_choice_zbi = Institution.objects.filter(type='zbiórka lokalna')
        sum_bags = Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
        sum_institutions = Donation.objects.aggregate(Count('institution'))['institution__count']
        return render(request, 'portfoliolab_app/index.html',
                      {'institutions_choice_fund': institutions_choice_fund,
                       'institutions_choice_org': institutions_choice_org,
                       'institutions_choice_zbi': institutions_choice_zbi,
                       'sum_bags': sum_bags, 'sum_institutions': sum_institutions})


class AddDonationView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/register.html')

