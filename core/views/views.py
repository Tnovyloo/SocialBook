import django.contrib.auth.forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from core.models import Profile, Post, Friends1, LikePost, Comment, FriendRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordResetForm
from itertools import chain
import logging
from ..forms import PostForm

@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    # user_profile = Profile.objects.get(user=user_object)
    posts = Post.objects.all()
    user_friend_requests = FriendRequest.objects.filter(receiver=user_object.id)

    context = {
        'user_profile': user_object,
        'posts': posts,
        'user_friend_requests': user_friend_requests
    }

    return render(request, 'index.html', context)

@login_required(login_url='signin')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user_id=pk)
    friends = Friends1.objects.get(current_user=user_object.id).users1.all()
    count_friends = len(friends)
    if_friends = friends.filter(id=request.user.id).exists()

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_friends': friends,
        'count_friends': count_friends,
        'if_friends': if_friends,
    }
    # logging(user_friends)

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
        # form = PostForm(request.FILES,
        #                 Profile.objects.get(user=request.user),
        #                 request.user.username)
        # if form.is_valid():
        #     new_post = form.save(commit=False)
        #     new_post.save()

        user = request.user.username
        image = request.FILES.get('image_upload')

        # caption = request.POST['caption']

        new_post = Post.objects.create(user_id=user,
                                       image=image,
                                       profile=Profile.objects.get(user=request.user)
                                       )
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='signin')
def comment(request):
    if request.method == 'POST':
        user = request.user
        post_id = request.POST['post_id']
        text = request.POST['text']
        new_comment = Comment.objects.create(post=Post.objects.get(id=post_id),
                                             profile=Profile.objects.get(user=user),
                                             content=text)
        new_comment.save()
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

@login_required(login_url='signin')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    search_question = request.POST['username']

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = [users.id for users in username_object]
        username_profile_list = [Profile.objects.filter(id_user=id) for id in username_profile]

        username_profile_list = list(chain(*username_profile_list))

    context = {
        'user_profile': user_profile,
        'username_profile_list': username_profile_list,
        'search_question': search_question,
    }

    return render(request, 'search.html', context)

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