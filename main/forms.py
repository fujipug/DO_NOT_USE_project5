from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import MyUser, Post


date_widget = {
    'birth': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
    }


class UserForm(UserCreationForm):
    model = User
    fields = ['username', 'password']


class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['email', 'name', 'zipcode']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)