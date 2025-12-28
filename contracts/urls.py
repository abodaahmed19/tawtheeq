from django.urls import path
from . import views

urlpatterns = [
    path('', views.contracts, name='contracts'),
    path('create/', views.contracts_create, name='contracts_create'),
    path('<int:contract_id>/edit/', views.contracts_edit, name='contracts_edit'),
]
