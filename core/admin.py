from django.contrib import admin
from .models import Profile, Friend_Request, Post, LikePost, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Friend_Request)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(Comment)