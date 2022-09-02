from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from ads.models import Ad, Category
from users.models import User


class AdSerializer(serializers.ModelSerializer):
    author_id = serializers.SlugRelatedField(
        required=False,
        queryset=Ad.objects.all(),
        slug_field='username'
    )
    category_id = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    author_id = serializers.SlugRelatedField(
        required=False,
        queryset=Ad.objects.all(),
        slug_field='username'
    )
    category_id = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._author_id = self.initial_data.pop('author_id')
        self._category_id = self.initial_data.pop('category_id')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ad = Ad.objects.create(
            name=validated_data.get('name'),
            price=validated_data.get('price'),
            description=validated_data.get('description'),
            is_published=validated_data.get('is_published')
        )

        ad.author_id = get_object_or_404(User, pk=self._author_id)
        ad.category_id = get_object_or_404(Category, pk=self._category_id)

        ad.save()

        return ad


class AdUpdateSerializer(serializers.ModelSerializer):
    author_id = serializers.SlugRelatedField(
        required=False,
        queryset=Ad.objects.all(),
        slug_field='username'
    )
    category_id = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._author_id = self.initial_data.pop('author_id')
        self._category_id = self.initial_data.pop('category_id')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        ad = super().save()

        ad.author_id = get_object_or_404(User, pk=self._author_id)
        ad.category_id = get_object_or_404(Category, pk=self._category_id)

        ad.save()

        return ad


class AdDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id']


class CatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        cat = Category.objects.create(
            name=validated_data.get('name')
        )

        cat.save()

        return cat


class CatUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def save(self):
        cat = super().save()

        return cat


class CatDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id']
