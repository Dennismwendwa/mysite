from django.db import models
from distutils.command.upload import upload
from email.policy import default


# Create your models here.


class countries(models.Model):


    name = models.CharField(max_length=100)
    population = models.IntegerField( )
    area = models.IntegerField( )
    capiatal_city = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')


