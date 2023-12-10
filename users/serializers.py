from rest_framework.serializers import ModelSerializer

from users.models import User, Science, Block


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ScienceModelSerializer(ModelSerializer):
    class Meta:
        model = Science
        fields = '__all__'


class BlockModelSerializer(ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'
