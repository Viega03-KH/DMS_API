from django.contrib import admin
from .models import IncomingDocument, Attachment, Journal, DeliveryType, Sender
# Register your models here.

admin.site.register([IncomingDocument, Attachment, Journal, DeliveryType, Sender])