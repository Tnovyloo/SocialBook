from django.contrib import admin
from .models import Profile, Friends1, Post, LikePost, Comment, FriendRequest
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Friends1)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(Comment)
admin.site.register(FriendRequest)
