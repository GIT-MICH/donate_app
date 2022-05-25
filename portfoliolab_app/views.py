from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.db.models import Sum, Count

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from portfoliolab_app.forms import DonationModelForm
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

    def post(self, request):
        form = DonationModelForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user
            donation.save()
            return redirect('confirmation')
        return render(request, 'portfoliolab_app/form.html', {'form': form})


class ConfirmationView(View):
    def get(self, request):
        return render(request, 'portfoliolab_app/form-confirmation.html')


class UserPageView(View):
    def get(self, request):
        user = request.user
        user_donations = Donation.objects.filter(user=user)
        return render(request, 'portfoliolab_app/user-page.html', {'user_donations': user_donations})

    def post(self, request):
        user = request.user
        user_donations = Donation.objects.filter(user=user)
        return render(request, 'portfoliolab_app/user-page.html', {'user_donations': user_donations})


class UserPageDetailView(View):
    def get(self, request, donation_id):
        user = request.user
        user_donations = Donation.objects.filter(user=user)
        donation_to_update = Donation.objects.get(id=donation_id)
        donation_to_update.is_taken = True
        donation_to_update.save()
        return render(request, 'portfoliolab_app/user-page.html', {'user_donations': user_donations, 'donation_to_update': donation_to_update})


@method_decorator(login_required, name='dispatch')
class ProtectedView(TemplateView):
    template_name = 'portfoliolab_app/form.html'
