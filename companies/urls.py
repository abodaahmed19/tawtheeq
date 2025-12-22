from django.urls import path
from . import views

urlpatterns = [
    path('', views.companies, name='companies'),
    path('create/', views.companies_create, name='companies_create'),
    path('<int:company_id>/edit/', views.companies_edit, name='companies_edit'),

]
