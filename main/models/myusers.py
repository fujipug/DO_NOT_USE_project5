from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class MyUser(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField(max_length=75)
    name = models.CharField(max_length=200)
    #state = models.CharField(max_length=75)
    #city = models.CharField(max_length=75)
    #birth = models.DateField()
    zipcode_validatior = RegexValidator(regex='^\d{5}(?:[-\s]\d{4})?$')
    zipcode = models.CharField(validators=[zipcode_validatior], max_length=5)