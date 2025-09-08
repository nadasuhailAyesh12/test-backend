from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(models.Model):
    ACTION_TYPES = [
        ('new_assignment', 'New Assignment'),
        ('assignment_graded', 'Assignment Graded'),
        ('new_announcement', 'New Announcement'),
        ('new_lecture', 'New Lecture'),
    ]

    TARGET_TYPES = [
        ('assignment', 'Assignment'),
        ('lecture', 'Lecture'),
        ('announcement', 'Announcement'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    action_type = models.CharField(max_length=50, choices=ACTION_TYPES)
    target_type = models.CharField(max_length=50, choices=TARGET_TYPES)
    target_id = models.IntegerField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.title}"
