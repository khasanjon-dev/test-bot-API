from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from users.models import Science, Block


class UserSerializer(Serializer):
    id = serializers.IntegerField(required=False)
    telegram_id = serializers.IntegerField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)


class ScienceModelSerializer(ModelSerializer):
    class Meta:
        model = Science
        fields = ('id', 'name', 'size', 'keys', 'author')


class BlockModelSerializer(ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'
