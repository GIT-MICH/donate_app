from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.db.models import Sum, Count

from portfoliolab_app.models import Donation, Institution, Account, Category


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


class AddDonationView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'portfoliolab_app/form.html', {'categories': categories, 'institutions': institutions})


class ConfirmationView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/form-confirmation.html')
