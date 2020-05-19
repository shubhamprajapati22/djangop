from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

class userData(models.Model):   #for inheriting the feature of database

    profileImg = models.ImageField(upload_to='Fpics', null = True)
    age = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
