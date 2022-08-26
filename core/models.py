from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    # bio = models.TextField(blank=True)

    #Profile images
    profile_img = models.ImageField(upload_to='profile_images',
                                    default='pexels-charles-1851164.jpg')
    wallpaper_img = models.ImageField(upload_to='wallpaper_images',
                                      default='pexels-amber-janssens-7327624.jpg')

    #Places where user live.
    location = models.CharField(max_length=100, blank=True)
    current_location = models.CharField(max_length=100, blank=True)

    #Education
    school = models.CharField(max_length=100, blank=True)

    #Contact info
    number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True)

    #Basic info
    gender = models.CharField(max_length=100, blank=True)
    birthday = models.CharField(max_length=50, blank=True)
    birthyear = models.CharField(max_length=4, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    user_id = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_media')
    created_at = models.DateTimeField(default=datetime.now())
    number_of_likes = models.IntegerField(default=0)
    caption = models.TextField()

    def __str__(self):
        return self.username