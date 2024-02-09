from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from tests.models import Block
from tests.serializers import BlockModelSerializer


class BlockModelViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockModelSerializer
