from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Kategoria')


class Institution(models.Model):
    FUNDACJA = 'fundacja'
    ORGANIZACJA_POZARZADOWA = 'organizacja pozarządowa'
    ZBIORKA_LOKALNA = 'zbiórka lokalna'

    TYPES = (
        (FUNDACJA, 'fundacja'),
        (ORGANIZACJA_POZARZADOWA, 'organizacja pozarządowa'),
        (ZBIORKA_LOKALNA, 'zbiórka lokalna')
    )

    name = models.CharField(max_length=256, verbose_name='Nazwa instytucji')
    decription = models.TextField()
    type = models.CharField(max_length=32, choices=TYPES, default=FUNDACJA)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=32)
    zip_code = models.IntegerField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField(auto_now=False)
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
