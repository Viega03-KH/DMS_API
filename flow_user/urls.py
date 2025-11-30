# flow_user/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CustomUserViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'departments', DepartmentViewSet, basename='department')

urlpatterns = [
    path('', include(router.urls)),
]
