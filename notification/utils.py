from turtle import pos
from .models import Notification

def create_notification(sender, to_user, notification_type, post=None):
    notification = Notification.objects.create(to_user=to_user, notification_type=notification_type, created_by=sender, post=post)
    