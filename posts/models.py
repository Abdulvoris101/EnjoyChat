from distutils.command.upload import upload
from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import Profile
from django.urls import reverse_lazy
import os

class Post(models.Model):
    content = models.TextField()
    image = models.FileField(upload_to='posts/', validators=[
                              FileExtensionValidator(['png', 'jpg', 'webp', 'jpeg', 'mp4', 'mkv'])])
    thumbnail_image = models.ImageField(upload_to='thumb/', blank=True)
    liked = models.ManyToManyField(Profile, blank=True, related_name='likes')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return str(self.content[:20])

    def num_likes(self):
        return self.liked.all().count()
    
    def num_comments(self):
        return self.comment_set.all().count()
    
    def get_absolute_url(self):
        return f'http://localhost:8000/post/{self.id}'
    
    def media_type(self):
        name, extension = os.path.splitext(self.image.name)
        image_ext = ['.png', '.jpg', '.jpeg', '.webp']
        video_ext = ['.mp4', '.mkv']

        for ext in image_ext:
            if ext == extension:
                return 'image'
        
        for ext in video_ext:
            if ext == extension:
                return 'video'
    


    class Meta:
        ordering = ('-created_at', )


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        ordering = ('-created_at', )


LIKE_CHOISES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOISES, max_length=8)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post} liked by {self.user} - {self.value}"

VERIFICATION_CHOISES = (
    ('Received', 'Received'),
    ('Verified', 'Verified')
)

class Verification(models.Model):

    class Job(models.IntegerChoices):
        BlogerActor = 1, "Bloger/Actor"
        Programmer = 2, "Programmer"
        FPlayer = 3, "Football Player"
        Sportsman = 4, "Sportsman"
        IT = 5, "Motion/Designer/IT",
        Other = 6, 'Other'

    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=255)
    verificated = models.CharField(
        choices=VERIFICATION_CHOISES,
        max_length=8,
        default='Received',
    )

    job = models.PositiveSmallIntegerField(
        choices=Job.choices,
        default=Job.Other
    )

    def __str__(self):
        return self.profile.user.username + '-' +  self.verificated

