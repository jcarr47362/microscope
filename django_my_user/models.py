from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True, default=0)
    displayname = models.TextField(max_length=240, default="")
