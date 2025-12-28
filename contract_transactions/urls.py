from django.urls import path
from . import views

urlpatterns = [
    path('', views.contract_transactions, name='contract_transactions'),
    path('create/', views.contract_transactions_create, name='contract_transactions_create'),
    path('<int:contract_transaction_id>/edit/', views.contract_transactions_edit, name='contract_transactions_edit'),
]
