from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('users/create/', views.users_create, name='users_create'),
    path('users/<int:user_id>/edit/', views.users_edit, name='users_edit'),
    path('profile/', views.profile, name='profile'),
]
