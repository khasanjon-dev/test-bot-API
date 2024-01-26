from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserModelViewSet, ScienceModelViewSet, BlockModelViewSet, AnswerScienceModelViewSet

router = DefaultRouter()
router.register('user', UserModelViewSet, 'user')
router.register('science', ScienceModelViewSet, 'science')
router.register('block', BlockModelViewSet, 'block')
router.register('answer-science', AnswerScienceModelViewSet, 'answer_science')
urlpatterns = [
    path('', include(router.urls))
]
