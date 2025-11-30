from django.contrib.auth.models import AbstractUser
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

def user_profile_path(instance, filename):
    return f'profile_images/{instance.id}/{filename}'

class CustomUser(AbstractUser):
    department = models.ForeignKey(
    Department, 
    on_delete=models.SET_NULL, 
    null=True, 
    blank=True, 
    related_name="users"
    )
    profile_image = models.ImageField(
        upload_to=user_profile_path, 
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username
