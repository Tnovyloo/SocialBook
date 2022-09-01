from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from . import settings_views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('upload', views.upload, name='upload'),
    path('settings', views.settings, name='settings'),
    path('like_post', views.like_post, name='like_post'),
    # Settings paths. TODO change profile picture.
    path('profile_basic_info', settings_views.profile_basic_info, name='profile_basic_info'),
    path('profile_location', settings_views.profile_location, name='profile_location'),
    path('profile_hobby', settings_views.profile_hobby, name='profile_hobby'),
    path('profile_contact', settings_views.profile_contact, name='profile_contact'),
    path('profile_relationship', settings_views.profile_relationship, name='profile_relationship'),
    path('profile_password', settings_views.profile_password, name='profile_password'),
    path('change_profile_image', settings_views.change_profile_image, name='change_profile_image'),
    # Friends request paths.
    path('send_friend_request/<int:userID>/', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:requestID>/', views.accept_friend_request, name='accept_friend_request'),
    path('friend_request', views.friend_request, name='friend_request')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)