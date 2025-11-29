from django.db import models
from flow_user.models import CustomUser

# ==== Lookup / Directory Models ====
class DeliveryType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name
class Journal(models.Model):
    name = models.TextField(unique=True)
    def __str__(self):
        return self.name[:50]
class Sender(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name


# ==== Main Document Model ====
class IncomingDocument(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
    ]
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="documents",
        blank=True, null=True
    )
    in_number = models.CharField(max_length=50, blank=True, null=True)
    in_date = models.DateField(blank=True, null=True)
    out_number = models.CharField(max_length=50, blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    delivery_type = models.ForeignKey(
        DeliveryType,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name="documents"
    )
    signer = models.CharField(max_length=255, blank=True, null=True)
    journal = models.ForeignKey(
        Journal,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name="documents"
    )
    title = models.TextField()
    sender = models.ForeignKey(
        Sender,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name="documents"
    )
    summary = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
        blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user'],
                condition=models.Q(status='draft'),
                name='unique_draft_per_user'
            )
        ]
    def __str__(self):
        return f"{self.id} - {self.title[:50]}"


# ==== Attachment Model ====
class Attachment(models.Model):
    document = models.ForeignKey(
        IncomingDocument,
        on_delete=models.CASCADE,
        related_name="attachments"
    )
    file = models.FileField(upload_to="attachments/")
    extension = models.CharField(max_length=10, null=True, blank=True)
    def save(self, *args, **kwargs):
        if self.file and not self.extension:
            self.extension = self.file.name.split('.')[-1]
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.file.name} ({self.document.in_number})"
    
