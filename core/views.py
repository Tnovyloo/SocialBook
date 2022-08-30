import django.contrib.auth.forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Post, Friend_Request
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordResetForm

# Create your views here.
@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    posts = Post.objects.all()

    context = {
        'user_profile': user_profile,
        'posts': posts,
    }

    return render(request, 'index.html', context)

@login_required(login_url='signin')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    #TODO

    # user_posts = Post.objects.filter(user_id=pk)
    # user_posts = Post.objects.filter(user_id=pk)
    # user_post_length = len(user_posts)
    #
    # follower = request.user.username
    # user = pk
    # user = User.objects.get(username=request.username)
    # if user.objects.friends.filter()
    #     button_text = 'Unfollow'
    # else:
    #     button_text = 'Follow'
    #
    # user_followers = len(FollowersCount.objects.filter(user=pk))
    # user_following = len(FollowersCount.objects.filter(follower=pk))

    # posts = Post.objects.all() #todo user posts

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        # 'posts': posts,
        # 'button_text': button_text
    }

    return render(request, 'profile.html', context)

@login_required(login_url='signin')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        # caption = request.POST['caption']

        new_post = Post.objects.create(user_id=user, image=image)
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'settings.html', {'user_profile': user_profile})

def friend_request(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'friend_request.html')

@login_required(login_url='signin')
def send_friend_request(request, userID):
    from_user = request.user
    to_user = User.objects.get(id=userID)
    friend_request, created = Friend_Request.objects.get_or_create(from_user=from_user, to_user=to_user)
    if created:
        return HttpResponse('friend request sent')
    else:
        return HttpResponse('friend request was already sent')

@login_required(login_url='signin')
def accept_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('friend request not accepted')

@login_required(login_url='signin')
def profile_basic_info(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        gender = request.POST['gender']
        birthdate = request.POST['birthdate']

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
            form = PasswordResetForm()
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                # messages.success(request, 'Your password was successfilyy updated!')
                return redirect('settings')
        else:
            messages.error(request, 'Passwords dont match.')
    return render(request, 'settings.html', {'user_profile': user_profile})

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        if password == password2 and first_name is not None and last_name is not None:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email was taken.')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username was taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()

                #Login user and redirect to settings page.
                user_login = auth.authenticate(username=username,
                                               password=password)
                auth.login(request, user_login)

                #Create a Profile object for a user.
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings') # TODO redirect to settings
        else:
            messages.info(request, "Password is not matching / First name and last name cannot be empty!")
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')