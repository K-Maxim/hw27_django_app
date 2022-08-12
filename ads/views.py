import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category


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
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        ads_data = json.loads(request.body)
        ad = Ad()
        ad.name = ads_data.get("name")
        ad.author = ads_data.get("author")
        ad.price = ads_data.get("price")
        ad.description = ads_data.get("description")
        ad.address = ads_data.get("address")
        ad.is_published = ads_data.get("is_published")

        ad.save()

        return JsonResponse({
            "id": ad.pk,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        }, safe=False)


class AdDetailView(DetailView):
    model = Ad()

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({
            "id": ad.pk,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        }, safe=False)


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
    model = Category()

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({
            "id": cat.pk,
            "name": cat.name,
        }, safe=False)
