from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserModelViewSet

router = DefaultRouter()
router.register('', UserModelViewSet, 'users')
urlpatterns = [
    path('', include(router.urls))
]
