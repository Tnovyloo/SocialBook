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

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.CharField(max_length=100, null=True)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    image = models.ImageField(upload_to='post_media')
    created_at = models.DateTimeField(default=datetime.now())
    number_of_likes = models.IntegerField(default=0)
    caption = models.TextField()

    def __str__(self):
        return str(self.user_id)

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    content = models.TextField(null=True)

    # TODO create image field which is null by default but when user upload image then show it in comment.

    def __str__(self):
        return str(self.post.id)

class Friends1(models.Model):
    users1 = models.ManyToManyField(User, null=True)
    current_user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE, null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, create = cls.objects.get_or_create(
                            current_user=current_user
                                                    )
        friend.users1.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, create = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users1.remove(new_friend)

class FriendRequest(models.Model):
    sender = models.ForeignKey(User, null=True, related_name='sender1', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    # def __str__(self):
    #     return str(sender + ' to ' + receiver)

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username