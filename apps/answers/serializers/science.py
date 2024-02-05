from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from answers.models import AnswerScience


class AnswerScienceModelSerializer(ModelSerializer):
    class Meta:
        model = AnswerScience
        fields = '__all__'


class GetAnswerSerializer(Serializer):
    user = serializers.IntegerField()
    test = serializers.IntegerField()
