from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from answers.models import AnswerScience


class AnswerScienceModelSerializer(ModelSerializer):
    class Meta:
        model = AnswerScience
        fields = ('true_answers', 'false_answers', 'science', 'user', 'size', 'created_at')


class GetAnswerSerializer(Serializer):
    user = serializers.IntegerField()
    science = serializers.IntegerField()
