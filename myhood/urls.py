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
    path('edit_profile/', views.edit_profile, name='edit-profile'),
    path('create_hood/', views.create_hood, name='create-hood'),
    path('create_business/<int:pk>/', views.create_business, name='create-business'),
    path('create_post/<int:pk>/', views.create_post, name='create-post'),
    path('hood_detail/<int:pk>/', views.hood_detail, name='hood-detail'),
    # path('hood/<int:pk>/', HoodDetailView.as_view(), name='hood-detail'),
    path('edit_profile/<int:pk>/', views.edit_profile, name='edit-profile'),
]