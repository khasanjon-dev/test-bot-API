from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Science, Block, Answer


class UserSerializer(Serializer):
    id = serializers.IntegerField(required=False)
    telegram_id = serializers.IntegerField(required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)


class ScienceModelSerializer(ModelSerializer):
    class Meta:
        model = Science
        fields = ('id', 'name', 'keys', 'size', 'author', 'created_at')


class BlockModelSerializer(ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'


class AnswerModelSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class CheckScienceSerializer(ModelSerializer):
    class Meta:
        model = Science
        fields = ('id', 'keys')
