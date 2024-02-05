from rest_framework.serializers import ModelSerializer

from tests.models import Science


class ScienceModelSerializer(ModelSerializer):
    class Meta:
        model = Science
        fields = ('id', 'name', 'keys', 'size', 'is_active', 'author', 'created_at')
