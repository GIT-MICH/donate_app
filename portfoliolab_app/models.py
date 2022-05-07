from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Kategoria')


class Institution(models.Model):
    name = models.CharField(max_length=256, verbose_name='Nazwa instytucji')
    decription = models.TextField()

    FUNDACJA = 'fundacja'
    ORGANIZACJA_POZARZADOWA = 'organizacja pozarządowa'
    ZBIORKA_LOKALNA = 'zbiórka lokalna'

    TYPES = (
        (FUNDACJA, 'fundacja'),
        (ORGANIZACJA_POZARZADOWA, 'organizacja pozarządowa'),
        (ZBIORKA_LOKALNA, 'zbiórka lokalna')
    )
    type = models.CharField(max_length=32, choices=TYPES, default=FUNDACJA)
    categories = models.ManyToManyField(Category)
