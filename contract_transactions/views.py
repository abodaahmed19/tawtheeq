from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from helpers.utils import role_required
from .models import ContractTransaction
from contract_transaction_types.models import ContractTransactionType
from contracts.models import Contract

# Contract Transactions
@role_required('admin')
def contract_transactions(request):
    contract_transactions = ContractTransaction.objects.all()
    not_complated_transactions = ContractTransaction.objects.filter(is_documented=False) # need edit
    complated_transactions = ContractTransaction.objects.filter(is_documented=False) # need edit
    documented_transactions = ContractTransaction.objects.filter(is_documented=True)

    return render(request, 'contract_transactions/index.html', {
        'contract_transactions': contract_transactions,
        'not_complated_transactions': not_complated_transactions,
        'complated_transactions': complated_transactions,
        'documented_transactions': documented_transactions
    })

# Create Contract Transaction
@role_required('admin')
def contract_transactions_create(request):
    contracts = Contract.objects.all()
    contract_transaction_types = ContractTransactionType.objects.all()

    contract_id = request.POST.get('contract_id', '')
    type_id = request.POST.get('type_id', '')
    date = request.POST.get('date', '')
    incoming_number = request.POST.get('incoming_number', '')
    extract_number = request.POST.get('extract_number', '')
    subject = request.POST.get('subject', '')
    
    if request.method == 'POST':
        contract_id = request.POST.get('contract_id')
        type_id = request.POST.get('type_id')
        date = request.POST.get('date')
        incoming_number = request.POST.get('incoming_number') or None
        extract_number = request.POST.get('extract_number') or None
        subject = request.POST.get('subject') or None

        contract_transaction = ContractTransaction(contract_id=contract_id,type_id=type_id,date=date,incoming_number=incoming_number,extract_number=extract_number,subject=subject)
        contract_transaction.save()
        messages.success(request, f"تم إنشاء معاملة العقد {contract_transaction.contract.name} ({contract_transaction.contract.number}) بنجاح")
        return redirect('contract_transactions')

    return render(request, 'contract_transactions/create.html', {
        'contracts': contracts,
        'contract_transaction_types': contract_transaction_types,
        'contract_id': contract_id,
        'type_id': type_id,
        'date': date,
        'incoming_number': incoming_number,
        'extract_number': extract_number,
        'subject': subject
    })

# Edit Contract Transaction
@role_required('admin')
def contract_transactions_edit(request, contract_transaction_id):
    contracts = Contract.objects.all()
    contract_transaction_types = ContractTransactionType.objects.all()

    contract_transaction = get_object_or_404(ContractTransaction, id=contract_transaction_id)

    contract_id = contract_transaction.contract_id
    type_id = contract_transaction.type_id
    date = contract_transaction.date
    incoming_number = contract_transaction.incoming_number
    extract_number = contract_transaction.extract_number
    subject = contract_transaction.subject

    if request.method == 'POST':
        contract_id = request.POST.get('contract_id', '').strip()
        type_id = request.POST.get('type_id', '').strip()
        date = request.POST.get('date', '').strip()
        incoming_number = request.POST.get('incoming_number', '').strip()
        extract_number = request.POST.get('extract_number', '').strip()
        subject = request.POST.get('subject', '').strip()

        contract_transaction.contract_id = contract_id
        contract_transaction.type_id = type_id
        contract_transaction.date = date
        contract_transaction.incoming_number = incoming_number
        contract_transaction.extract_number = extract_number
        contract_transaction.subject = subject
        contract_transaction.save()

        messages.success(request, f"تم تعديل معاملة العقد {contract_transaction.contract.name} ({contract_transaction.contract.number}) بنجاح")
        return redirect('contract_transactions')

    return render(request, 'contract_transactions/edit.html', {
        'contracts': contracts,
        'contract_transaction_types': contract_transaction_types,
        'contract_transaction': contract_transaction,
        'contract_id': contract_id,
        'type_id': type_id,
        'date': date,
        'incoming_number': incoming_number,
        'extract_number': extract_number,
        'subject': subject
    })
