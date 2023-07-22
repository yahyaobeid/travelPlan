from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USERNAME_FIELD='username'
    name = models.CharField(max_length=300)
    username=models.CharField(unique=True, max_length=200, default="")
    email = models.EmailField()
    password = models.CharField(max_length=300)
    confirm_password = models.CharField(max_length=300)
    last_login = models.DateTimeField(auto_now=True, null=True)
    is_superuser = models.BooleanField(default=False)

    is_anonymous=models.BooleanField(default=True)
    is_authenticated=models.BooleanField(default=True)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email