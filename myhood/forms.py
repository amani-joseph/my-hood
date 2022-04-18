from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Neighbourhood, Business, Post


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name', 'city_address', 'location', 'description', ]
        exclude = ('user', 'population_count')
        labels = {
            'name': ('Neighborhood name'),
            'city_address': ('City Address'),
        }
        help_texts = {
            'city_address': ('City, street, estate/building'),
            # 'location': ('Do not fill this field manually'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Neighborhood name'}),
            'city_address': forms.TextInput(attrs={'placeholder': 'City, street, estate/building'}),
            'location': forms.TextInput(attrs={'placeholder': "CLICK THE MAP BELOW - DON'T ADD LOCATION BY TYPING! "}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter description here'}),
        }
        


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'email', 'address',  'categories', 'location']
        exclude = ('user', 'neighbourhood')


class PostForm(forms.ModelForm):
    '''
    Class that handles creating neighborhood posts
    '''
    class Meta:
        model = Post
        fields = ['image', 'message']
        exclude = [ "pub_date", "user"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','hood']