from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
    path('tests/', include('tests.urls')),
    path('answers/', include('answers.urls'))
]
