from django.urls import path, include
from rest_framework.routers import DefaultRouter

from answers.views import AnswerScienceModelViewSet

routers = DefaultRouter()
routers.register('science', AnswerScienceModelViewSet, 'answers')

urlpatterns = [
    path('', include(routers.urls))
]
