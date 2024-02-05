from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import User
from users.serializers import UserSerializer


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
