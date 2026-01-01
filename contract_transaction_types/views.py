from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from helpers.utils import role_required
from .models import ContractTransactionType
from contract_transaction_requirements.models import ContractTransactionRequirement

# Contract Transactions
@role_required('admin')
def contract_transaction_types(request):
    contract_transaction_types = ContractTransactionType.objects.all()
    
    return render(request, 'contract_transaction_types/index.html', {
        'contract_transaction_types': contract_transaction_types,
    })

# Create Contract Transaction
@role_required('admin')
def contract_transaction_types_create(request):
    name = request.POST.get('name', '')

    if request.method == 'POST':
        name = request.POST.get('name')
        requirements = request.POST.getlist('requirements[]')

        contract_transaction_type = ContractTransactionType(name=name)
        contract_transaction_type.save()

        contract_transaction_type_id = contract_transaction_type.id

        for req in requirements:
            if req.strip():
                ContractTransactionRequirement.objects.create(
                    name=req,
                    type_id=contract_transaction_type_id
                )

        messages.success(request, f"تم إنشاء نوع معاملة العقد {contract_transaction_type.name} بنجاح")
        return redirect('contract_transaction_types')

    return render(request, 'contract_transaction_types/create.html', {
        'name': name
    })

# Edit Contract Transaction
@role_required('admin')
def contract_transaction_types_edit(request, contract_transaction_type_id):
    contract_transaction_type = get_object_or_404(ContractTransactionType, id=contract_transaction_type_id)

    name = contract_transaction_type.name
    requirements = ContractTransactionRequirement.objects.filter(type_id=contract_transaction_type.id)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()

        contract_transaction_type.name = name
        contract_transaction_type.save()

        messages.success(request, f"تم تعديل نوع معاملة العقد {contract.name} بنجاح")
        return redirect('contract_transaction_types')

    return render(request, 'contract_transaction_types/edit.html', {
        'contract_transaction_type': contract_transaction_type,
        'name': name,
        'requirements': requirements
    })
