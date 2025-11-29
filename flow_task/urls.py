from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, SubjectViewSet

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet, basename='subjects')
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]
