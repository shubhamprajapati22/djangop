from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

class UserData(models.Model):   #for inheriting the feature of database

    profileImg = models.ImageField(upload_to='Fpics', default = 'Fpics/userpic.gif')
    age = models.IntegerField(null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
