from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from answers.models import AnswerScience
from users.models import User


class AnswerScienceModelSerializer(ModelSerializer):
    class Meta:
        model = AnswerScience
        fields = ('false_keys', 'science', 'user', 'size', 'score', 'created_at', 'owner_id')


class GetAnswerScienceSerializer(Serializer):
    user = serializers.IntegerField()
    science = serializers.IntegerField()


class UserScoreSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class SinceScoreSerializer(ModelSerializer):
    user = UserScoreSerializer(read_only=True)

    class Meta:
        model = AnswerScience
        fields = ('user', 'score', 'created_at')
