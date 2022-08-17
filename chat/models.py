from tabnanny import verbose
from django.db import models
from django.dispatch import receiver

class ChatModel(models.Model):
    sender = models.CharField(max_length=100, default=None)
    message = models.TextField(null=True, blank=True, default='')
    img_src = models.CharField(null=True, blank=True, max_length=500)
    room_name = models.CharField(null=True, blank=True, max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}-{self.message}'
    
    class Meta:
        verbose_name = 'Chat message'
        verbose_name_plural = 'Chat messages'
    
class ChatImageUpload(models.Model):
    sender = models.CharField(max_length=255)
    image = models.ImageField(upload_to='chat/images/')
    room_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.sender} room is {self.room_name}'