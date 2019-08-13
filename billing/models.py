from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    icon = models.ImageField()

