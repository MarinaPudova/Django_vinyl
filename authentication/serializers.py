from djoser.serializers import UserSerializer as BaseUserSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

from rest_framework import serializers

from authentication.models import Gender


class UserSerializer(BaseUserSerializer):

    birth_date = serializers.DateField()
    phone_number = serializers.CharField()
    gender = serializers.ChoiceField([(gender.name, gender.value) for gender in Gender])
    country = serializers.CharField()
    city = serializers.CharField()

    class Meta(BaseUserSerializer.Meta):
        fields = ('id', 'gender', 'first_name', 'last_name', 'username', 'birth_date', 'email',
                  'phone_number', 'country', 'city')


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('id', 'gender', 'first_name', 'last_name', 'username', 'birth_date', 'email', 'password',
                  'phone_number', 'country', 'city')
