from django.urls import path, include
from .views import IncomingDocumentDraftCreateView, IncomingDocumentViewSet, AttachmentViewSet, DeliveryTypeViewSet, JournalViewSet, SenderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'documents', IncomingDocumentViewSet, basename='document')
router.register(r'attachments', AttachmentViewSet, basename='attachment')
router.register(r'delivery-types', DeliveryTypeViewSet)
router.register(r'journals', JournalViewSet)
router.register(r'senders', SenderViewSet)

urlpatterns = [
    path('documents/draft/', IncomingDocumentDraftCreateView.as_view(), name='document-draft-create'),  # faqat POST
]

urlpatterns += [
    path('', include(router.urls)),  # ViewSet endpointlar
]
