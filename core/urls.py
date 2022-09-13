from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from . import views_settings
from . import views_friends
from . import views_about

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
    path('settings', views_settings.settings, name='settings'),
    path('profile_basic_info', views_settings.profile_basic_info, name='profile_basic_info'),
    path('profile_location', views_settings.profile_location, name='profile_location'),
    path('profile_hobby', views_settings.profile_hobby, name='profile_hobby'),
    path('profile_contact', views_settings.profile_contact, name='profile_contact'),
    path('profile_relationship', views_settings.profile_relationship, name='profile_relationship'),
    path('profile_password', views_settings.profile_password, name='profile_password'),
    path('change_profile_image', views_settings.change_profile_image, name='change_profile_image'),
    # Friends request paths.
    path('friend_request/<str:pk>/', views_friends.friend_request, name='friend_request'),
    path('add_or_remove_friend/<str:pk>/<str:operation>', views_friends.add_or_remove_friend, name='add_or_remove_friend'),
    path('delete_request/<str:pk>/<str:operation>', views_friends.delete_request, name='delete_request'),
    # About section - edit buttons.
    path('about_current_place', views_about.about_current_place, name='about_current_place'),
    path('about_from_place', views_about.about_from_place, name='about_from_place'),
    path('about_school', views_about.about_school, name='about_school'),
    path('about_hobby', views_about.about_hobby, name='about_hobby'),
    path('about_number', views_about.about_number, name='about_number'),
    path('about_email', views_about.about_email, name='about_email'),
    path('about_gender', views_about.about_gender, name='about_gender'),
    path('about_birthyear', views_about.about_birthyear, name='birthyear'),
    path('about_relationship', views_about.about_relationship, name='about_relationship'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)