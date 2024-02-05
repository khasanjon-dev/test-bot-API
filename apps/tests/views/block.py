from rest_framework.viewsets import ModelViewSet

from tests.models import Block
from tests.serializers import BlockModelSerializer


class BlockModelViewSet(ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockModelSerializer
