import django.contrib.auth.forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from core.models import Profile, Post, Friends1, LikePost, Comment, FriendRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

def friend_request(request, pk):
    sender = User.objects.get(username=request.user.username)
    recipient = User.objects.get(username=pk)
    model = FriendRequest.objects.get_or_create(sender=sender, receiver=recipient)
    return redirect(f'/')

def delete_request(request, operation, pk):
    client1 = User.objects.get(username=pk)
    print(client1)
    if operation == 'Sender_deleting':
        model1 = FriendRequest.objects.get(sender=request.user, receiver=client1)
        model1.delete()
    elif operation == 'Receiver_deleting':
        model2 = FriendRequest.objects.get(sender=client1, receiver=request.user)
        model2.delete()
        return redirect('/')

    return redirect('/')

def add_or_remove_friend(request, operation, pk):
    new_friend = User.objects.get(username=pk)
    if operation == 'add':
        fq = FriendRequest.objects.get(sender=new_friend, receiver=request.user)
        Friends1.make_friend(request.user, new_friend)
        Friends1.make_friend(new_friend, request.user)
        fq.delete()
    elif operation == 'remove':
        Friends1.lose_friend(request.user, new_friend)
        Friends1.lose_friend(new_friend, request.user)

    return redirect('/')