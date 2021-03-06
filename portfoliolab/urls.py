"""portfoliolab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from portfoliolab_app.views import ( LandingPageView,
                                     AddDonationView,
                                     ConfirmationView,
                                     UserPageView,
                                     UserPageDetailView
                                     )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('add_donation/', AddDonationView.as_view(), name='add-donation'),
    path('confirmation/', ConfirmationView.as_view(), name='confirmation'),
    path('user/', UserPageView.as_view(), name='user-page'),
    path('user/<int:donation_id>/', UserPageDetailView.as_view(), name='user-detail'),
    path('accounts/', include('accounts.urls'))
]
