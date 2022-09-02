from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_related_name')
    friends = models.ManyToManyField(User, blank=True)

    id_user = models.IntegerField()
    # bio = models.TextField(blank=True)

    #Profile images
    profile_img = models.ImageField(upload_to='profile_images',
                                    default='user-profile-icon.jpg')
    wallpaper_img = models.ImageField(upload_to='wallpaper_images',
                                      default='wallpaper_default.jpg')

    #Places where user live.
    location = models.CharField(max_length=100, blank=True)
    current_location = models.CharField(max_length=100, blank=True)

    #Education
    school = models.CharField(max_length=100, blank=True)
    hobby = models.CharField(max_length=100, blank=True)

    #Contact info
    number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)

    #Basic info
    gender = models.CharField(max_length=100, blank=True)
    birthday = models.CharField(max_length=50, blank=True)
    birthyear = models.CharField(max_length=4, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    relationship = models.CharField(max_length=50, blank=True)
    family = models.CharField(max_length=50, blank=True)

    #TODO to my profile create many to many user to posts field

    def __str__(self):
        return self.user.username

class Friend_Request(models.Model):
    from_user = models.ForeignKey(
        User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name='to_user', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_media')
    created_at = models.DateTimeField(default=datetime.now())
    number_of_likes = models.IntegerField(default=0)
    caption = models.TextField()

    def __str__(self):
        return self.user_id

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username