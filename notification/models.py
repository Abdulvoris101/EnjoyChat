from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from posts.models import Post

class Notification(models.Model):
    FOLLOWER = 'follower'
    LIKE = 'like'
    COMMENT = 'comment'
    MESSAGE = 'message'

    CHOICES = (
        (FOLLOWER, 'Follower'),
        (LIKE, 'Like'),
        (COMMENT, 'Comment'),
        (MESSAGE, 'Message')
    )

    to_user = models.ForeignKey(Profile, related_name='notifications', on_delete=models.CASCADE)

    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Profile, related_name='creatednotifications', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
