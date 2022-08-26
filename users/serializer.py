from rest_framework import serializers

from users.models import User, Location


class UserList_or_RetrieveSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop('location_id')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for loc in self._location:
            loc_object, _ = Location.objects.get_or_create(name=loc)
            user.location_id.add(loc_object)

        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop('location_id')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for loc in self._location:
            loc_object, _ = Location.objects.get_or_create(name=loc)
            user.location_id.add(loc_object)

        user.save()
        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
