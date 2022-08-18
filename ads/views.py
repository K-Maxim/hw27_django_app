import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.shortcuts import render, get_object_or_404

from ads.models import Ad, Category
from users.models import User


def source_page(request):
    return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        ads = Ad.objects.all()
        response = []

        for ad in ads:
            response.append({
                "id": ad.pk,
                "name": ad.name,
                "author": ad.author.username,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "image": ad.image.url,
                "category": ad.category_id.name,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)

        author = User.objects.get(pk=ad_data["author_id"])
        category = Category.objects.get(pk=ad_data["category_id"])

        ad = Ad.objects.create(
            name=ad_data["name"],
            author=author,
            price=ad_data["price"],
            description=ad_data["description"],
            category_id=category,
        )

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "price": ad.price,
            "description": ad.description,
            # "category_id": ad.category_id,
        }, safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({
            "id": ad.pk,
            "name": ad.name,
            "author": ad.author_id,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url,
            "category": ad.category_id.name,
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad

    fields = ['name', 'author', 'price', 'description', 'category_id']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad_data = json.loads(request.body)

        self.object.name = ad_data["name"]
        self.object.price = ad_data["price"]
        self.object.description = ad_data["description"]

        self.object.save()

        return JsonResponse({
            "id": self.object.pk,
            "name": self.object.name,
            "author": self.object.author,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url,
            "category": self.object.category_id.name,
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad

    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            "status": "ok"
        }, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CatView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = []

        for category in categories:
            response.append({
                "id": category.pk,
                "name": category.name,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        cat_data = json.loads(request.body)
        cat = Category()

        cat.name = cat_data["name"]

        cat.save()

        return JsonResponse({
            "id": cat.id,
            "name": cat.name
        })


class CatDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({
            "id": cat.pk,
            "name": cat.name,
        }, safe=False)
