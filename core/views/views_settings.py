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
def settings(request):
    user_object = User.objects.get(username=request.user)
    user_profile = Profile.objects.get(user=user_object)
    return render(request, 'settings.html', {'user_profile': user_profile})

@login_required(login_url='signin')
def change_profile_image(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        profile_img = request.FILES.get('profile_image')
        user_profile.profile_img = profile_img
        user_profile.save()
        return redirect('settings')
    else:
        return render(request, 'settings.html', {'user_profile': user_profile})

@login_required(login_url='signin')
def profile_basic_info(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        gender = request.POST['gender']
        birthdate = request.POST['birthdate']
        profile_img = request.FILES.get('profile_image')


        if first_name is not None:
            user_profile.first_name = first_name
        if last_name is not None:
            user_profile.last_name = last_name
        if gender is not None:
            user_profile.gender = gender

        # if birthdate is not None:
        #     day = str(birthdate).split('-')[0:1]
        #     year = str(birthdate).split('-')[2]
        #     user_profile.birthday = day
        #     user_profile.year = year

        user_profile.save()
        return redirect('settings')
    else:
        return render(request, 'settings.html', {'user_profile': user_profile})

@login_required(login_url='signin')
def profile_location(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        live_place = request.POST['liveplace']
        from_place = request.POST['from']
        if live_place is not None:
            user_profile.current_location = live_place
        if from_place is not None:
            user_profile.location = from_place

        user_profile.save()
        return redirect('settings')
    else:
        return render(request, 'settings.html', {'user_profile': user_profile})


@login_required(login_url='signin')
def profile_hobby(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        hobby = request.POST['hobby']
        school = request.POST['school']
        if hobby is not None:
            user_profile.hobby = hobby
        if school is not None:
            user_profile.school = school

        user_profile.save()
        return redirect('settings')
    else:
        return render(request, 'settings.html', {'user_profile': user_profile})

@login_required(login_url='signin')
def profile_contact(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        number = request.POST['number']
        email = request.POST['email']
        if number is not None:
            user_profile.number = number
        if email is not None:
            user_profile.email = email

        user_profile.save()
        return redirect('settings')
    else:
        return render(request, 'settings.html', {'user_profile': user_profile})

@login_required(login_url='signin')
def profile_relationship(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        relationship = request.POST['relationship']
        family = request.POST['family']
        if relationship is not None:
            user_profile.relationship = relationship
        if family is not None:
            user_profile.family = family

        user_profile.save()
        return redirect('settings')
    else:
        return render(request, 'settings.html', {'user_profile': user_profile})

@login_required(login_url='signin')
def profile_password(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        if new_password == new_password2:
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                # messages.success(request, 'Your password was successfilyy updated!')
                return redirect('settings')
        else:
            messages.error(request, 'Passwords dont match.')
    return render(request, 'settings.html', {'user_profile': user_profile})