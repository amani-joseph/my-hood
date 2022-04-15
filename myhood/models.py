from django.db import models
from django.forms import EmailField, ImageField
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from location_field.models.plain import PlainLocationField
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('profile/' )
    bio = models.TextField(max_length=300, null=True, default="My Bio", blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save( *args, **kwargs)


class Neighbourhood(models.Model):
     city = models.CharField(max_length=100)
     location = PlainLocationField(based_fields=['city'], zoom=7)
     title = models.CharField(max_length=100)
     description = models.TextField(max_length=400)
     user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
     categories = (
          ('school', 'school'),
          ('gym', 'gym'),
          ('gas-station', 'gas-station'),
          ('recreational', 'recreational'),
          ('religious', 'religious'),
          ('business', 'business'),
          ('shop', 'shop'),
          ('shopping-center', 'shopping-center'),
          ('residential', 'residential'),
          
     )
     category = models.CharField(choices=categories, max_length=100, default="", blank=True)
     Neighbourhood_location = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='category', null=True)
