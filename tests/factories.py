import factory.django

from ads.models import Ad, Category
from users.models import User


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = 'password'
    email = factory.Faker('name')


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = 'minimum of 10 characters'
    author_id = factory.SubFactory(AuthorFactory)
    price = 500
    category_id = factory.SubFactory(CategoryFactory)
    is_published = False
