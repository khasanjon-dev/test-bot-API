from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="TEST BOT API",
        default_version='v1',
        contact=openapi.Contact(email="khasanjon.dev@gmail.com"),
    ),
    public=True,
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('admin/', admin.site.urls),
    path('api/', include('apps.urls'))
]
