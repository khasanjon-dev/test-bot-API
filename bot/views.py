from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import User, Science, Block, Answer
from .serializers import ScienceModelSerializer, BlockModelSerializer, UserSerializer, AnswerModelSerializer, \
    CheckScienceSerializer
from .utils import keys_serializer


class UserModelViewSet(ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(['post'], False, 'get-or-create')
    def get_or_create_user(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        telegram_id = serializer.data.get('telegram_id')
        if User.objects.filter(telegram_id=telegram_id).exists():
            User.objects.filter(telegram_id=telegram_id).update(**serializer.data)
            user = User.objects.get(telegram_id=telegram_id)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        User.objects.create(**serializer.data)
        user = User.objects.get(telegram_id=telegram_id)
        serializer = self.get_serializer(user)
        return Response(serializer.data, 201)

    @action(['post'], False, 'get-user')
    def get_user(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        telegram_id = serializer.data.get('telegram_id')
        user = get_object_or_404(User, telegram_id=telegram_id)
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class ScienceModelViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Science.objects.all()
    serializer_class = ScienceModelSerializer

    @action(['post'], False, 'check-answer', serializer_class=CheckScienceSerializer)
    def check_answer(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        science = get_object_or_404(Science, id=serializer.data['id'])
        keys_author = keys_serializer(science.keys)
        keys_user = keys_serializer(serializer.data['keys'])


class BlockModelViewSet(ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockModelSerializer


class CheckAnswerModelViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerModelSerializer
