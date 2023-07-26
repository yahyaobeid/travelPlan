from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import JSONField

class User(AbstractUser):
    USERNAME_FIELD='username'
    name = models.CharField(max_length=300)
    username=models.CharField(unique=True, max_length=200, default="")
    email = models.EmailField()
    password = models.CharField(max_length=300)
    confirm_password = models.CharField(max_length=300)
    profile_pic = models.ImageField(upload_to='images/profile_pictures', blank=True)
    bio = models.CharField(max_length=700)
    location=models.CharField(max_length=150, blank=True)
    last_login = models.DateTimeField(auto_now=True, null=True)
    is_superuser = models.BooleanField(default=False)

    is_anonymous=models.BooleanField(default=True)
    is_authenticated=models.BooleanField(default=True)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
class TravelPlan(models.Model):
    destination = models.CharField(max_length=200)
    days = models.IntegerField()
    data = models.JSONField()

    def __str__(self):
        return self.destination

