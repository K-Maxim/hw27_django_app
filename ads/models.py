from django.db import models

# Create your models here.


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=5000)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
