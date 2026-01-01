from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from helpers.utils import role_required
from contract_transactions.models import ContractTransaction

# Documentation
@role_required('admin')
def automated_documentation(request):
    contract_transactions = ContractTransaction.objects.all() # need edit
    complated_transactions = ContractTransaction.objects.filter(is_documented=False) # need edit
    documented_transactions = ContractTransaction.objects.filter(is_documented=True)

    return render(request, 'automated_documentation/index.html', {
        'contract_transactions': contract_transactions,
        'complated_transactions': complated_transactions,
        'documented_transactions': documented_transactions
    })
