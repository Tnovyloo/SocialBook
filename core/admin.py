from django.contrib import admin
from .models import Profile, Friends1, Post, LikePost, Comment, FriendRequest

# Register your models here.
admin.site.register(Profile)
admin.site.register(Friends1)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(Comment)
admin.site.register(FriendRequest)
