from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
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


# @login_required
def profile(request):
    return render(request, 'myhood/auth/profile.html')


# @login_required
def edit_profile(request):
    return render(request, 'myhood/auth/edit-profile.html')
