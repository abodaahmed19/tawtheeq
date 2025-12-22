from django.urls import path
from . import views

urlpatterns = [
    path('', views.departments, name='departments'),
    path('create/', views.departments_create, name='departments_create'),
    path('<int:department_id>/edit/', views.departments_edit, name='departments_edit'),
    path('by_parent/', views.departments_by_parent, name='departments_by_parent'),
]
