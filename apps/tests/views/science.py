from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from tests.models import Science
from tests.serializers import ScienceModelSerializer


class ScienceModelViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Science.objects.all()
    serializer_class = ScienceModelSerializer
