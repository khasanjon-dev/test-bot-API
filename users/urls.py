from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserModelViewSet, ScienceModelViewSet, BlockModelViewSet

router = DefaultRouter()
router.register('user', UserModelViewSet, 'user')
router.register('science', ScienceModelViewSet, 'science')
# router.register('block', BlockModelViewSet, 'block')
urlpatterns = [
    path('', include(router.urls))
]
