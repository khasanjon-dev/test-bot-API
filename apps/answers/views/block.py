from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from answers.models import AnswerBlock
from answers.serializers import AnswerBlockModelSerializer, GetAnswerBlockSerializer


class AnswerBlockViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = AnswerBlock.objects.all()
    serializer_class = AnswerBlockModelSerializer

    @action(['post'], False, 'get-answer', serializer_class=GetAnswerBlockSerializer)
    def get(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        answer = get_object_or_404(AnswerBlock, block=serializer.data['block'], user=serializer.data['user'])
        serializer = AnswerBlockModelSerializer(answer)
        return Response(serializer.data)
