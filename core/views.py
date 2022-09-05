import django.contrib.auth.forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Post, Friend_Request, LikePost
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordResetForm

@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    posts = Post.objects.all()

    #TODO connect posts with post.user_id profile.image

    context = {
        'user_profile': user_profile,
        'posts': posts,
    }

    return render(request, 'index.html', context)
# Create your views here.

@login_required(login_url='signin')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user_id=pk)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        # 'button_text': button_text
    }

    return render(request, 'profile.html', context)

@login_required(login_url='signin')
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user.username == post.user_id:
        post_to_delete = Post.objects.get(id=post_id)
        post_to_delete.delete()
        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='signin')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        # caption = request.POST['caption']

        new_post = Post.objects.create(user_id=user, image=image, profile=Profile.objects.get(user=request.user))
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter is None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.number_of_likes = post.number_of_likes + 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.number_of_likes = post.number_of_likes - 1
        post.save()
        return redirect('/')

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
                new_profile = Profile.objects.create(user=user_model,
                                                     id_user=user_model.id,
                                                     email=None,
                                                     first_name=first_name,
                                                     last_name=last_name)
                new_profile.save()
                return redirect('settings')
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