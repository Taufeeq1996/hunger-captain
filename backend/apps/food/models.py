from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Food(models.Model):

    name = models.CharField('name', max_length=30, blank=False, null=False) 

    price = models.PositiveIntegerField('price', default = 0, blank=False, null=False) 

    image = CloudinaryField('image', blank=True, null=True)  