import django.contrib.auth.forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from core.models import Profile, Post, Friends1, LikePost
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

@login_required(login_url='signin')
def about_current_place(request):
    profile_name = request.POST['profile_name']
    user = request.user.username
    user_object = User.objects.get(username=user)
    if request.method == 'POST':
        if user_object.username == profile_name:
            prev_place = user_object.profile.current_location
            new_place = request.POST['live_place']
            if new_place != prev_place:
                user_object.profile.current_location = new_place
                user_object.profile.save()
                return redirect(f'/profile/{user}')
            else:
                return redirect(f'/profile/{user}')
        else:
            return redirect(f'/profile/{user}')
    else:
        return redirect(f'/profile/{user}')

@login_required(login_url='signin')
def about_from_place(request):
    profile_name = request.POST['profile_name']
    user = request.user.username
    user_object = User.objects.get(username=user)
    if request.method == 'POST':
        if user_object.username == profile_name:
            prev_variable = user_object.profile.location
            new_variable = request.POST['from_place']
            if new_variable != prev_variable:
                user_object.profile.location = new_variable
                user_object.profile.save()
                return redirect(f'/profile/{user}')
            else:
                return redirect(f'/profile/{user}')
        else:
            return redirect(f'/profile/{user}')
    else:
        return redirect(f'/profile/{user}')

@login_required(login_url='signin')
def about_school(request):
    profile_name = request.POST['profile_name']
    user = request.user.username
    user_object = User.objects.get(username=user)
    if request.method == 'POST':
        if user_object.username == profile_name:
            prev_variable = user_object.profile.school
            new_variable = request.POST['school']
            if new_variable != prev_variable:
                user_object.profile.school = new_variable
                user_object.profile.save()
                return redirect(f'/profile/{user}')
            else:
                return redirect(f'/profile/{user}')
        else:
            return redirect(f'/profile/{user}')
    else:
        return redirect(f'/profile/{user}')

@login_required(login_url='signin')
def about_hobby(request):
    profile_name = request.POST['profile_name']
    user = request.user.username
    user_object = User.objects.get(username=user)
    if request.method == 'POST':
        if user_object.username == profile_name:
            prev_variable = user_object.profile.hobby
            new_variable = request.POST['hobby']
            if new_variable != prev_variable:
                user_object.profile.hobby = new_variable
                user_object.profile.save()
                return redirect(f'/profile/{user}')
            else:
                return redirect(f'/profile/{user}')
        else:
            return redirect(f'/profile/{user}')
    else:
        return redirect(f'/profile/{user}')

@login_required(login_url='signin')
def about_number(request):
    profile_name = request.POST['profile_name']
    user = request.user.username
    user_object = User.objects.get(username=user)
    if request.method == 'POST':
        if user_object.username == profile_name:
            prev_variable = user_object.profile.number
            new_variable = request.POST['number']
            if new_variable != prev_variable:
                user_object.profile.number = new_variable
                user_object.profile.save()
                return redirect(f'/profile/{user}')
            else:
                return redirect(f'/profile/{user}')
        else:
            return redirect(f'/profile/{user}')
    else:
        return redirect(f'/profile/{user}')

@login_required(login_url='signin')
def about_email(request):
    profile_name = request.POST['profile_name']
    user = request.user.username
    user_object = User.objects.get(username=user)
    if request.method == 'POST':
        if user_object.username == profile_name:
            prev_variable = user_object.profile.email
            new_variable = request.POST['email']
            if new_variable != prev_variable:
                user_object.profile.email = new_variable
                user_object.profile.save()
                return redirect(f'/profile/{user}')
            else:
                return redirect(f'/profile/{user}')
        else:
            return redirect(f'/profile/{user}')
    else:
        return redirect(f'/profile/{user}')

@login_required(login_url='signin')
def about_gender(request):
    profile_name = request.POST['profile_name']
    user = request.user.username
    user_object = User.objects.get(username=user)
    if request.method == 'POST':
        if user_object.username == profile_name:
            prev_variable = user_object.profile.gender
            new_variable = request.POST['gender']
            if new_variable != prev_variable:
                user_object.profile.gender = new_variable
                user_object.profile.save()
                return redirect(f'/profile/{user}')
            else:
                return redirect(f'/profile/{user}')
        else:
            return redirect(f'/profile/{user}')
    else:
        return redirect(f'/profile/{user}')

@login_required(login_url='signin')
def about_birthyear(request):
    profile_name = request.POST['profile_name']
    user = request.user.username
    user_object = User.objects.get(username=user)
    if request.method == 'POST':
        if user_object.username == profile_name:
            prev_variable = user_object.profile.birthyear
            new_variable = request.POST['birthyear']
            if new_variable != prev_variable:
                user_object.profile.birthyear = new_variable
                user_object.profile.save()
                return redirect(f'/profile/{user}')
            else:
                return redirect(f'/profile/{user}')
        else:
            return redirect(f'/profile/{user}')
    else:
        return redirect(f'/profile/{user}')

@login_required(login_url='signin')
def about_relationship(request):
    profile_name = request.POST['profile_name']
    user = request.user.username
    user_object = User.objects.get(username=user)
    if request.method == 'POST':
        if user_object.username == profile_name:
            prev_variable = user_object.profile.relationship
            new_variable = request.POST['relationship']
            if new_variable != prev_variable:
                user_object.profile.relationship = new_variable
                user_object.profile.save()
                return redirect(f'/profile/{user}')
            else:
                return redirect(f'/profile/{user}')
        else:
            return redirect(f'/profile/{user}')
    else:
        return redirect(f'/profile/{user}')