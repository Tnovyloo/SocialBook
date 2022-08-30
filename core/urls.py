from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('upload', views.upload, name='upload'),
    path('settings', views.settings, name='settings'),
    # Settings paths. TODO change profile picture.
    path('profile_basic_info', views.profile_basic_info, name='profile_basic_info'),
    path('profile_location', views.profile_location, name='profile_location'),
    path('profile_hobby', views.profile_hobby, name='profile_hobby'),
    path('profile_contact', views.profile_contact, name='profile_contact'),
    path('profile_relationship', views.profile_relationship, name='profile_relationship'),
    path('profile_password', views.profile_password, name='profile_password'),
    # Friends request paths.
    path('send_friend_request/<int:userID>/', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:requestID>/', views.accept_friend_request, name='accept_friend_request'),
    path('friend_request', views.friend_request, name='friend_request')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)