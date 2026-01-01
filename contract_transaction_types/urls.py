from django.urls import path
from . import views

urlpatterns = [
    path('', views.contract_transaction_types, name='contract_transaction_types'),
    path('create/', views.contract_transaction_types_create, name='contract_transaction_types_create'),
    path('<int:contract_transaction_type_id>/edit/', views.contract_transaction_types_edit, name='contract_transaction_types_edit'),
]
