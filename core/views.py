import django.contrib.auth.forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Post
from django.contrib.auth.decorators import login_required

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

    # if FollowersCount.objects.filter(follower=follower, user=user).first():
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
        # 'posts': posts
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

@login_required(login_url='signin')
def profile_basic_info(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        gender = request.POST['gender']
        birthdate = request.POST['birthdate']

        post_data = (first_name, last_name, gender, birthdate)
        profile_data = (user_profile.first_name, user_profile.last_name,
                        user_profile.gender, user_profile.birthdate)

    pass

@login_required(login_url='signin')
def profile_location(request):
    pass

@login_required(login_url='signin')
def profile_hobby(request):
    pass

@login_required(login_url='signin')
def profile_contact(request):
    pass

@login_required(login_url='signin')
def profile_relationship(request):
    pass

@login_required(login_url='signin')
def profile_password(request):
    pass


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