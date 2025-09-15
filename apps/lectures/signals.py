from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Lecture
from django.core.mail import send_mail
@receiver(post_save, sender=Lecture)
def send_lecture_notification(sender, instance, created, **kwargs):
    if created:
        print("📢 Notification: New lecture added →", instance.title)

        channel_layer = get_channel_layer()
        data = {
            "title": instance.title,
            "teacher": instance.teacher.user.get_full_name(),
            "message": "new Lecture"
        }
        async_to_sync(channel_layer.group_send)(
            "students_group",  
            {
                "type": "lecture_notification",
                "data": data
            }
        )
        # Email notification
        send_mail(
        subject='📚 New Lecture Available',
        message=f'''
         A new lecture has been uploaded.

        Title: {instance.title}
        Description: {instance.description}
        Video Link: {instance.video or "Not available"}
        PDF File: {instance.pdf or "Not available"}
        ''',
       from_email='noreply@yourdomain.com',
       recipient_list=['student1@example.com', 'student2@example.com'],  # ← adjust as needed
       fail_silently=False
       )
