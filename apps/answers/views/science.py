from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from answers.models import AnswerScience
from answers.serializers import AnswerScienceModelSerializer, GetAnswerSerializer


class AnswerScienceModelViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin, GenericViewSet):
    queryset = AnswerScience.objects.all()
    serializer_class = AnswerScienceModelSerializer

    @action(['post'], False, 'get-answer', serializer_class=GetAnswerSerializer)
    def get(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        answer = get_object_or_404(AnswerScience, test=serializer.data['test'], user=serializer.data['user'])
        serializer = AnswerScienceModelSerializer(answer)
        return Response(serializer.data)
