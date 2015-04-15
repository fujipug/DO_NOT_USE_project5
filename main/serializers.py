from django.forms import widgets
from rest_framework import serializers
from main.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'username', 'title', 'body', 'created')