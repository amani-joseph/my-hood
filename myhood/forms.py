from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Neighbourhood, Business


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name', 'city_address', 'description', ]
        exclude = ('user', 'population_count')


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'email', 'address', 'categories']
        exclude = ('user', 'neighbourhood', 'location')
