from django.contrib.auth.models import AbstractUser
from django.db import models
from users.validators import age_verification, mail_verification


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
