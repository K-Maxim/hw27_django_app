from rest_framework import serializers

from ads.models import Ad, Category


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
