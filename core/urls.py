from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from . import settings_views
from . import friends_views
from . import about_views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('upload', views.upload, name='upload'),
    path('search', views.search, name='search'),
    path('like_post', views.like_post, name='like_post'),
    path('delete_post/<post_id>', views.delete_post, name='delete_post'),
    path('comment', views.comment, name='comment'),
    # Settings paths. TODO change profile picture.
    path('settings', settings_views.settings, name='settings'),
    path('profile_basic_info', settings_views.profile_basic_info, name='profile_basic_info'),
    path('profile_location', settings_views.profile_location, name='profile_location'),
    path('profile_hobby', settings_views.profile_hobby, name='profile_hobby'),
    path('profile_contact', settings_views.profile_contact, name='profile_contact'),
    path('profile_relationship', settings_views.profile_relationship, name='profile_relationship'),
    path('profile_password', settings_views.profile_password, name='profile_password'),
    path('change_profile_image', settings_views.change_profile_image, name='change_profile_image'),
    # Friends request paths.
    path('friend_request/<str:pk>/', friends_views.friend_request, name='friend_request'),
    path('add_or_remove_friend/<str:pk>/<str:operation>', friends_views.add_or_remove_friend, name='add_or_remove_friend'),
    path('delete_request/<str:pk>/<str:operation>', friends_views.delete_request, name='delete_request'),
    # About section - edit buttons.
    # path('about_current_place/<str:pk>/<str:new_place>', about_views.about_current_place, name='about_current_place'),
    path('about_current_place', about_views.about_current_place, name='about_current_place'),
    path('about_from_place', about_views.about_from_place, name='about_from_place'),
    path('about_school', about_views.about_school, name='about_school'),
    path('about_hobby', about_views.about_hobby, name='about_hobby'),
    path('about_number', about_views.about_number, name='about_number'),
    path('about_email', about_views.about_email, name='about_email'),
    path('about_gender', about_views.about_gender, name='about_gender'),
    path('about_birthyear', about_views.about_birthyear, name='birthyear'),
    path('about_relationship', about_views.about_relationship, name='about_relationship'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)