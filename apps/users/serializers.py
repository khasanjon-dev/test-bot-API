from rest_framework import serializers
from rest_framework.serializers import Serializer


class UserSerializer(Serializer):
    id = serializers.IntegerField(required=False)
    telegram_id = serializers.IntegerField(required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
