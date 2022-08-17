from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy


class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='no bio...')
    email = models.EmailField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatar.png')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    uptated_at = models.DateTimeField(auto_now_add=True)
    followed = models.ManyToManyField('self', blank=True, related_name='follow', symmetrical=False)
    last_seen = models.DateTimeField(blank=True, null=True)
    
    
    # get posts
    def get_posts_count(self):
        return self.posts.all().count()


    def get_all_author_posts(self):
        return self.posts.all()
    
    # Get given likes 
    def get_likes_given_count(self):
        likes = self.like_set.all()
        total_liked = 0
        for item in likes:
            if item.value == 'Like':
                total_liked += 1
        
        return total_liked
    
    def get_absolute_url(self):
        return reverse_lazy('profile', kwargs={'slug': self.slug})
    # get received likes

    def get_likes_received_no(self):
        posts = self.posts.all()
        total_liked = 0

        for item in posts:
            total_liked += item.liked.all().count()
            
        return total_liked
    
    def filtered_msgs(self):
        notifs = self.creatednotifications.filter(is_read=False, notification_type='message')
        return notifs

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        slug = slugify(str(self.user.username))
        self.slug = slug

        super().save(*args, **kwargs)


STATUS_CHOISES = (
    ('Follow', 'Follow'),
    ('Unfollow', 'Unfollow')
)


class RelationShipManager(models.Manager):
    def invatations_received(self, me):
        qs = RelationShip.objects.filter(status='follow').exclude(sender=me)
        return qs


class RelationShip(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOISES)
    created_at = models.DateTimeField(auto_now=True)
    uptated_at = models.DateTimeField(auto_now_add=True)

    objects = RelationShipManager()

    def __str__(self):
        return f'{self.sender}-to-{self.receiver}'