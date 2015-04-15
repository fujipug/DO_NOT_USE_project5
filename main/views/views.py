from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import MyUser, Post
from main.forms import UserForm, MyUserForm, SignInForm, PostForm
from main.serializers import PostSerializer
from rest_framework import generics


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def splash(request):
    return render(request, 'splash.html', {})


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def sign_up(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    elif request.method == 'POST':
        user_form = UserForm(request.POST)
        myuser_form = MyUserForm(request.POST)
        if all((user_form.is_valid(), myuser_form.is_valid())):
            new_user = user_form.save()
            new_myuser = myuser_form.save(commit=False)
            new_myuser.user = new_user
            new_myuser.save()
            return HttpResponseRedirect('/sign_in')
    else:
        user_form = UserForm()
        myuser_form = MyUserForm()
    return render(request, 'sign_up.html',
                  {'user_form': user_form, 'myuser_form': myuser_form})


def sign_in(request):
    error = ""
    if request.method == 'POST':
        sign_in_form = SignInForm(request.POST)
        if sign_in_form.is_valid():
            username = sign_in_form.cleaned_data["username"]
            password = sign_in_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:

                error = "Invalid username/password."
                form = SignInForm(initial={'username': request.POST.get('username')})
                # return HttpResponseRedirect('/sign_in/')
    elif request.method == 'GET':
        sign_in_form = SignInForm()
    else:
        return HttpResponseRedirect('/sign_in/')
    return render(request, "sign_in.html", {'sign_in_form': sign_in_form, 'error': error})


def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/home/')


def profile(request, id):
    if request.user.is_authenticated():
        return render(request, "profile.html",
                      {'logged_in_user': request.user.id,
                       'profile_user': User.objects.get(id=id),
                       'myuser': MyUser.objects.get(user=id), 'posts': Post.objects.all})
    else:
        return HttpResponseRedirect('/splash/')


def profiles(request):
    if request.user.is_authenticated():
        return render(request, "profiles.html",
                      {'users': MyUser.objects.all})
    else:
        return HttpResponseRedirect('/splash/')