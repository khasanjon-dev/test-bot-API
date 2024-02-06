from rest_framework.viewsets import ModelViewSet

from answers.models import AnswerBlock
from answers.serializers import AnswerBlockModelSerializer


class AnswerBlockViewSet(ModelViewSet):
    queryset = AnswerBlock.objects.all()
    serializer_class = AnswerBlockModelSerializer
