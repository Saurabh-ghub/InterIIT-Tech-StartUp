from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Interest(models.Model):
    profession = models.CharField(max_length=50)
    email = models.CharField( max_length=100)
    interest = models.CharField(max_length=200)

# Create your models here.
class StudentForm(models.Model):  
    email     = models.EmailField("Enter Email")  
    file      = models.FileField() # for creating file input  
    updated_at = models.DateTimeField(auto_now=True)