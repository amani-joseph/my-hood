from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('signup/', views.register, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='myhood/auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myhood/index.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('create_hood/', views.create_hood, name='create-hood'),
    path('edit_profile/<int:pk>', views.edit_profile, name='edit-profile'),
]