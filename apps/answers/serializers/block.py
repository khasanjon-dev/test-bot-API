from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from answers.models import AnswerBlock


class AnswerBlockModelSerializer(ModelSerializer):
    class Meta:
        model = AnswerBlock
        fields = '__all__'


class GetAnswerBlockSerializer(Serializer):
    user = serializers.IntegerField()
    block = serializers.IntegerField()
