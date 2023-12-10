from rest_framework.viewsets import ModelViewSet

from users.models import User, Science, Block
from users.serializers import UserModelSerializer, ScienceModelSerializer, BlockModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class ScienceModelViewSet(ModelViewSet):
    queryset = Science.objects.all()
    serializer_class = ScienceModelSerializer


class BlockModelViewSet(ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockModelSerializer
