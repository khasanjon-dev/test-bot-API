from django.urls import path, include
from rest_framework.routers import DefaultRouter

from answers.views import AnswerScienceModelViewSet, AnswerBlockViewSet

routers = DefaultRouter()
routers.register('science', AnswerScienceModelViewSet)
routers.register('block', AnswerBlockViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
