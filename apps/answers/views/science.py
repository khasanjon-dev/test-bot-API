from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from answers.models import AnswerScience
from answers.serializers import AnswerScienceModelSerializer, GetAnswerScienceSerializer, SinceScoreSerializer


class AnswerScienceModelViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = AnswerScience.objects.all()
    serializer_class = AnswerScienceModelSerializer

    @action(['post'], False, 'get-answer', serializer_class=GetAnswerScienceSerializer)
    def get(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        answer = get_object_or_404(AnswerScience, science=serializer.data['science'], user=serializer.data['user'])
        serializer = AnswerScienceModelSerializer(answer)
        return Response(serializer.data)

    @action(['get'], True, 'scores', serializer_class=SinceScoreSerializer)
    def get_scores(self, request, pk):
        """
        return user data for this test id

        ```
        """
        scores = AnswerScience.objects.filter(science_id=pk).order_by('created_at', '-false_keys')
        serializer = self.get_serializer(scores, many=True)
        return Response(serializer.data)


'''
1. Omonova Adibaxon - 160.4 ball 🥇
2. Hamroyev Asilbek - 148.5 ball 🥈
3. Isaqova Durdona - 142.4 ball 🥉
4. Ibodullayev Ilyosbek - 28.4 ball 
'''
