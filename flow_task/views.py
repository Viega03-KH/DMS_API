from rest_framework import viewsets
from .models import Task, Subject
from .serializers import TaskSerializer, SubjectSerializer
from rest_framework.pagination import PageNumberPagination

class TaskPagination(PageNumberPagination):
    page_size = 10  # har bir sahifada 10 ta Document
    page_size_query_param = 'page_size'
    max_page_size = 50

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
