from rest_framework.serializers import ModelSerializer

from tests.models import Block


class BlockModelSerializer(ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'
