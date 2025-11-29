from django.db import models
from flow_user.models import CustomUser
from flow_document.models import IncomingDocument  


class Subject(models.Model):
    title = models.CharField(max_length=250)
    def __str__(self):
        return self.title

class Task(models.Model):
    document = models.ForeignKey(
        IncomingDocument,
        on_delete=models.CASCADE,
        related_name="tasks",
        blank=True,
        null=True
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='tasks',
        blank=True,
        null=True
    )
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    assignees = models.ManyToManyField(
        CustomUser,
        related_name="assigned_tasks",
        blank=True
    )
    status_choices = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Task: {self.subject} (Document {self.document_id})"

