from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="Document Flow API",
        default_version='v1',
        description="Document Flow Project API documentation",
    ),
    public=True,  # Swagger UI hamma uchun ko‘rinadi
    permission_classes=[permissions.AllowAny],  # Swagger UI ochiq
    authentication_classes=[],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT endpoints
    path('api/token/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/auth/', TokenRefreshView.as_view(), name='token_refresh'),

    # flow_user app
    path('api/', include('flow_user.urls')),
    path('api/', include('flow_document.urls')),
    path('api/', include('flow_task.urls')),

    # Swagger va Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Statik va media fayllar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
