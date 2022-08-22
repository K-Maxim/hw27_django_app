from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


class User(models.Model):
    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Админ"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLES, default="member")
    age = models.IntegerField()
    location_id = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
