from rest_framework.serializers import ModelSerializer

from answers.models import AnswerBlock


class AnswerBlockModelSerializer(ModelSerializer):
    class Meta:
        model = AnswerBlock
        fields = ('true_answers', 'false_answers', 'block', 'user', 'size', 'created_at')
