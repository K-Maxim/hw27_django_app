from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


MIN_AGE = 9


def age_verification(value: date):
    quantity_month = date.today().year * 12 + date.today().month - value.year * 12 + value.month
    quantity_years = quantity_month / 12
    if quantity_years < 9:
        raise ValidationError(
            "Access denied",
            params={'value': value}
        )


def mail_verification(value):
    if 'rambler.ru' in value:
        raise ValidationError(
            f"Регистрация с почты rambler.ru запрещена",
            params={'value', value}
        )


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLES = [
        (MEMBER, "Пользователь"),
        (MODERATOR, "Модератор"),
        (ADMIN, "Админ"),
    ]

    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    # username = models.CharField(max_length=50, unique=True)
    # password = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLES, default=MEMBER)
    age = models.IntegerField(null=True)
    location_id = models.ManyToManyField(Location, null=True)

    birth_date = models.DateField(validators=[age_verification], null=True)
    email = models.EmailField(unique=True, validators=[mail_verification])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
