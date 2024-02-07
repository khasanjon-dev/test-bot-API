from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from answers.models import AnswerScience
from answers.serializers import AnswerScienceModelSerializer, GetAnswerScienceSerializer


class AnswerScienceModelViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin, GenericViewSet):
    queryset = AnswerScience.objects.all()
    serializer_class = AnswerScienceModelSerializer

    @action(['post'], False, 'get-answer', serializer_class=GetAnswerScienceSerializer)
    def get(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        answer = get_object_or_404(AnswerScience, science=serializer.data['science'], user=serializer.data['user'])
        serializer = AnswerScienceModelSerializer(answer)
        return Response(serializer.data)
