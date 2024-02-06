from rest_framework.serializers import ModelSerializer

from tests.models import Block


class BlockModelSerializer(ModelSerializer):
    class Meta:
        model = Block
        fields = ('id', 'keys', 'size', 'is_active', 'author', 'created_at')
