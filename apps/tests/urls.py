from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tests.views import BlockModelViewSet, ScienceModelViewSet

router = DefaultRouter()
router.register('block', BlockModelViewSet, 'blocks')
router.register('science', ScienceModelViewSet, 'sciences')
urlpatterns = [
    path('', include(router.urls))
]
