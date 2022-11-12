from distutils.command.upload import upload
from email.policy import default
from django.db import models





class Destination(models.Model):

    
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=300)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    
