from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    name = models.CharField(max_length=100, unique=True , default="Mr. S")
    bio = models.TextField(blank=True)
    office_hours = models.CharField(max_length=255, blank=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.get_full_name() or self.user.username    
    
class Lecture(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video = models.URLField(blank=True, null=True)
    pdf = CloudinaryField('pdf', resource_type='raw', blank=True, null=True)  

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lectures')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title