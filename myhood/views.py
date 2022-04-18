from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from myhood.models import Neighbourhood, Business
from .forms import UserRegisterForm, NeighbourHoodForm, BusinessForm,ProfileUpdateForm, UserUpdateForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.
def register(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
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
    view to render the index page.
    """
    title = 'My-Hood'
    context = {
        'title': title,
        'hoods': Neighbourhood.objects.all()

    }
    # return render(request, )
    return render(request, 'myhood/index.html', context)


@login_required
def create_hood(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = request.user
            hood.save()
            return redirect('index')
    else:
        form = NeighbourHoodForm()
    return render(request, 'myhood/hood_form.html', {'form': form})


@login_required
def hood_detail(request, pk):
    """_summary_

    Args:
        request (_type_): _description_
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    hood = Neighbourhood.objects.get(id=pk)
    businesses = Business.objects.filter(neighbourhood=hood)
    context = {
        'hood': hood,
        'businesses': businesses
    }
    return render(request, 'myhood/hood_detail.html', context)


@login_required
def create_business(request, pk):
    """_summary_

    Args:
        pk: the neighbourhood's id
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = request.user
            business.neighbourhood = Neighbourhood.objects.filter(id=pk).first()
            business.save()
            next = request.GET.get('next', reverse('index'))
            return HttpResponseRedirect(f'/hood_detail/{pk}/')
            # return redirect(f'hood_detail/{pk}')
    else:
        form = BusinessForm()
    return render(request, 'myhood/business_form.html', {'form': form})


def about(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, 'myhood/about.html')


@login_required
def profile(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    user = request.user
    context = {
        'user': user,
        'neighbourhood': Neighbourhood.objects.filter(user=request.user).all()
    }
    return render(request, 'myhood/auth/profile.html', context)


@login_required
def edit_profile(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'myhood/auth/edit-profile.html', context)

