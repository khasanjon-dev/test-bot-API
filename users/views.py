from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from users.models import User, Science, Block
from users.serializers import ScienceModelSerializer, BlockModelSerializer, UserSerializer


class UserModelViewSet(ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(['post'], False, 'get-or-create')
    def get_or_create(self, request):
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


class ScienceModelViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Science.objects.all()
    serializer_class = ScienceModelSerializer


class BlockModelViewSet(ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockModelSerializer
