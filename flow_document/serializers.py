from rest_framework import serializers
from .models import IncomingDocument, Attachment, DeliveryType, Journal, Sender

class DeliveryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryType
        fields = ['id', 'name']

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'name']

class SenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sender
        fields = ['id', 'name']

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'document', 'file', 'extension']
        read_only_fields = ['extension']

    def create(self, validated_data):
        # extension avtomatik saqlanadi save() da
        return super().create(validated_data)

class IncomingDocumentDrafSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomingDocument
        fields = ['user']

    def create(self, validated_data):
        user = validated_data['user']
        # Mavjud draftni olish yoki yangi yaratish
        draft, created = IncomingDocument.objects.get_or_create(
            user=user,
            status='draft',
            defaults={'status': 'draft'}
        )
        return draft

class IncomingDocumentSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True)
    delivery_type = DeliveryTypeSerializer(read_only=True)
    journal = JournalSerializer(read_only=True)
    sender = SenderSerializer(read_only=True)
    class Meta:
        model = IncomingDocument
        fields = '__all__'
    
