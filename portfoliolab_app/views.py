from django.shortcuts import render, reverse
from django.views import View
from django.db.models import Sum, Count

from portfoliolab_app.models import Donation


class LandingPageView(View):
    def get(self, request):
        sum_bags = Donation.objects.aggregate(Sum('quantity'))
        sum_bags = sum_bags['quantity__sum']
        sum_institutions = Donation.objects.annotate(num_institution=Count('institution_id'))
        # sum_institutions = sum_institutions[0].num_institution
        return render(request, 'portfoliolab_app/index.html', {'sum_bags': sum_bags, 'sum_institutions': sum_institutions})


class AddDonationView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/register.html')

