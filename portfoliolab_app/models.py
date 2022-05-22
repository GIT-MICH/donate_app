from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Account(AbstractUser):
        """Account model."""

        username = None
        email = models.EmailField(_('email address'), unique=True)

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = []
        objects = UserManager()


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Kategoria')

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.name


class Institution(models.Model):
    FUNDACJA = 'fundacja'
    ORGANIZACJA_POZARZADOWA = 'organizacja pozarządowa'
    ZBIORKA_LOKALNA = 'zbiórka lokalna'

    TYPES = [
        (FUNDACJA, 'fundacja'),
        (ORGANIZACJA_POZARZADOWA, 'organizacja pozarządowa'),
        (ZBIORKA_LOKALNA, 'zbiórka lokalna')
    ]

    name = models.CharField(max_length=256, verbose_name='Nazwa instytucji')
    decription = models.TextField()
    type = models.CharField(max_length=32, choices=TYPES, default=FUNDACJA)
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Instytucja'
        verbose_name_plural = 'Instytucje'

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=5)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField(auto_now=False)
    pick_up_comment = models.TextField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Darowizna'
        verbose_name_plural = 'Darowizny'

    def __str__(self):
        return self.institution.name
