from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from myhood.models import Neighbourhood
from .forms import UserRegisterForm # UserUpdateForm, ProfileUpdateForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created {username} \n welcome to myhood')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "myhood/auth/signup.html", {'form': form})


def index(request):
    """
    view to render the index.
    """
    title = 'My-Hood'
    context = {
        'title': title,

    }
    # return render(request, )
    return render(request, 'myhood/index.html')

def about(request):
    return render(request, 'myhood/about.html')


@login_required
def profile(request):
    user = request.user
    context = {
        'user': user,
        'neighbourhood': Neighbourhood.objects.filter(user=request.user).all()
    }
    return render(request, 'myhood/auth/profile.html', context)


# @login_required
def edit_profile(request):
    return render(request, 'myhood/auth/edit-profile.html')
