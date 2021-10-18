from django.db import models
from django.db.models import manager

# Create your models here.
class SignupMaster(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    dob=models.DateField()
    mobile=models.BigIntegerField()
    email=models.EmailField()
