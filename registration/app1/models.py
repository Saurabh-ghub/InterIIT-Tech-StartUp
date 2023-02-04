from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Interest(models.Model):
    email = models.CharField( max_length=100)
    interest = models.CharField(max_length=200)
