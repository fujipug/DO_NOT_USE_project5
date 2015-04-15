from django.db import models
from main.models import MyUser
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]


class Post(models.Model):
    user = models.ForeignKey(MyUser)
    username = models.CharField(max_length=200)
    title = models.CharField(max_length=32)
    body = models.TextField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)