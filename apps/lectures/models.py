from django.db import models
from django.conf import settings

# Create your models here.
class Level(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    name = models.CharField(max_length=20, choices=LEVEL_CHOICES, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    office_hours = models.CharField(max_length=255, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username    
    
class Lecture(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video_url = models.CharField(max_length=500, blank=True)  
    pdf_url = models.CharField(max_length=500, blank=True)   
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='lectures')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lectures')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title