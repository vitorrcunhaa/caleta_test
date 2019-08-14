from django.db import models
from django.contrib.auth.models import User


class Cash(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    field = models.CharField(max_length=50)
    value = models.IntegerField()

