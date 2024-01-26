from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Science, Block, AnswerScience


class UserSerializer(Serializer):
    id = serializers.IntegerField(required=False)
    telegram_id = serializers.IntegerField(required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)


class ScienceModelSerializer(ModelSerializer):
    class Meta:
        model = Science
        fields = ('id', 'name', 'keys', 'size', 'is_active', 'author', 'created_at')


class BlockModelSerializer(ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'


class AnswerScienceModelSerializer(ModelSerializer):
    class Meta:
        model = AnswerScience
        fields = '__all__'


class GetAnswerSerializer(Serializer):
    user = serializers.IntegerField()
    test = serializers.IntegerField()
