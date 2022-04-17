from django.db import models
from django.forms import EmailField, ImageField
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.gis.geos import Point
from location_field.models.plain import PlainLocationField
from django.urls import reverse

# Create your models here.
categories = (
    ('business', 'business'),
    ('grocery', 'grocery'),
    ('gym', 'gym'),
    ('gas-station', 'gas-station'),
    ('hospital', 'hospital'),
    ('market', 'market'),
    ('recreational', 'recreational'),
    ('religious', 'religious'),
    ('residential', 'residential'),
    ('school', 'school'),
    ('shop', 'shop'),
    ('shopping-mall', 'shopping-mall'),
    ('sports', 'sports'),

)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('profile/')
    bio = models.TextField(max_length=300, null=True, default="My Bio", blank=True)
    hood = models.ForeignKey('Neighbourhood', null=True, on_delete=models.SET_NULL, default='')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)


class Neighbourhood(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default='')
    city_address = models.CharField(max_length=100)
    population_count = models.IntegerField(null=False, blank=False, default=0)
    location = PlainLocationField(based_fields=['city_address'], zoom=7)
    description = models.TextField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def search_project(cls, name):
        return cls.objects.filter(name__icontains=name).all()

    @classmethod
    def all_neighbourhoods(cls):
        return cls.objects.all()

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()


class Business(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default='')
    email = models.EmailField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=False, default='')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    location = PlainLocationField(based_fields=['address'], zoom=7, blank=False, default='')
    categories = models.CharField(choices=categories, max_length=100, default='', blank=True)
    def __str__(self):
        return f'{self.name}'

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

# class Category(models.Model):
#
#     category = models.CharField(choices=categories, max_length=100, default="", blank=True)
#     business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='category', null=True)
#
#     def __str__(self):
#         return f'{self.business_location}, category'

class Post(models.Model):
    
    message = models.CharField(max_length=200, null=False, unique=True, blank=True)
    image = CloudinaryField('posts/', null=True, blank=True )
    pub_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
    
    def save_post(self):
        self.save()
    
    def get_absolute_url(self):
        return reverse('index')