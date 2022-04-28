from django.db.models.signals import post_save
from django.dispatch import receiver
from pathlib import Path
from PIL import Image
import os
from .models import Post
import cv2
import random


BASE_DIR = str(Path(__file__).resolve().parent.parent)

@receiver(post_save, sender=Post)
def post_save_create_thumbnail(sender, instance, created, **kwargs):
    if created:
        post = Post.objects.get(pk=instance.pk)
        video_file = BASE_DIR + post.image.url.replace('/', '\\')
        thumbnail_dir = BASE_DIR + '\\media\\thumb\\'
        # print(post.media_type())
        
        img_name = f'{post.content}-{post.author.user}-{random.randrange(1, 9000)}'
        img_src = f'thumb/{img_name}'

        if (post.media_type() == 'video'): 
            print(img_name)
            cap = cv2.VideoCapture(video_file)
            cap.set(cv2.CAP_PROP_POS_MSEC, 1000)      # Go to the 1 sec. position
            ret, frame = cap.read()                   # Retrieves the frame at the specified second
            cv2.imwrite(thumbnail_dir + img_name + ".jpg", frame)
            post.thumbnail_image = img_src +  ".jpg"
            post.save()