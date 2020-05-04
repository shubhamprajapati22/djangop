from django.db import models

# Create your models here.

class family_d(models.Model):   #for inheriting the feature of database
    path_img = models.ImageField(upload_to='Fpics')
    h = models.BooleanField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
