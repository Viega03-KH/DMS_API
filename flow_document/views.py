from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import IncomingDocument, Attachment, DeliveryType, Journal, Sender
from .serializers import IncomingDocumentDrafSerializer, IncomingDocumentSerializer, AttachmentSerializer, DeliveryTypeSerializer, JournalSerializer, SenderSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser

class IncomingDocumentDraftCreateView(generics.CreateAPIView):
    queryset = IncomingDocument.objects.all()
    serializer_class = IncomingDocumentDrafSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        draft = serializer.save()
        return Response({"id": draft.id}, status=status.HTTP_201_CREATED)


class DocumentPagination(PageNumberPagination):
    page_size = 10  # har bir sahifada 10 ta Document
    page_size_query_param = 'page_size'
    max_page_size = 50


class IncomingDocumentViewSet(viewsets.ModelViewSet):
    queryset = IncomingDocument.objects.all()
    serializer_class = IncomingDocumentSerializer
    pagination_class = DocumentPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # faqat draft bo'lmagan hujjatlar
        return IncomingDocument.objects.exclude(status='draft')

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')  # Bir nechta fayl olish

        document_id = request.data.get("document")
        if not document_id:
            return Response(
                {"error": "document id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        created = []

        for file in files:
            serializer = self.get_serializer(data={
                "document": document_id,
                "file": file,
                "extension": file.name.split('.')[-1],
            })
            serializer.is_valid(raise_exception=True)
            serializer.save()
            created.append(serializer.data)

        return Response(created, status=status.HTTP_201_CREATED)



class DeliveryTypeViewSet(viewsets.ModelViewSet):
    queryset = DeliveryType.objects.all()
    serializer_class = DeliveryTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticated]


class SenderViewSet(viewsets.ModelViewSet):
    queryset = Sender.objects.all()
    serializer_class = SenderSerializer
    permission_classes = [permissions.IsAuthenticated]