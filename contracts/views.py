from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from helpers.utils import role_required
from .models import Contract
from companies.models import Company

# Contracts
@role_required('admin')
def contracts(request):
    contracts = Contract.objects.all()
    active_contracts = Contract.objects.filter(status='active')
    expired_contracts = Contract.objects.filter(status='expired')
    suspended_contracts = Contract.objects.filter(status='suspended')
    

    return render(request, 'contracts/index.html', {
        'contracts': contracts,
        'active_contracts': active_contracts,
        'expired_contracts': expired_contracts,
        'suspended_contracts': suspended_contracts
    })

# Create Contract
@role_required('admin')
def contracts_create(request):
    contractors = Company.objects.filter(type='contractor')
    consultants = Company.objects.filter(type='consultant')

    number = request.POST.get('number', '')
    name = request.POST.get('name', '')
    department_id = request.POST.get('department_id', '')
    amount = request.POST.get('amount', '')
    signing_date = request.POST.get('signing_date', '')
    site_handover_date = request.POST.get('site_handover_date', '')
    actual_start_date = request.POST.get('actual_start_date', '')
    duration = request.POST.get('duration', '')
    company_id = request.POST.get('company_id', '')
    
    if request.method == 'POST':
        number = request.POST.get('number')
        name = request.POST.get('name')
        department_id = request.POST.get('department_id')
        amount = request.POST.get('amount')
        signing_date = request.POST.get('signing_date')
        site_handover_date = request.POST.get('site_handover_date') or None
        actual_start_date = request.POST.get('actual_start_date') or None
        duration = request.POST.get('duration')
        company_id = request.POST.get('company_id')

        contract = Contract(number=number,name=name,department_id=department_id,amount=amount,signing_date=signing_date,site_handover_date=site_handover_date,actual_start_date=actual_start_date,duration=duration,company_id=company_id)
        contract.save()
        messages.success(request, f"تم إنشاء العقد {contract.name} بنجاح")
        return redirect('contracts')

    return render(request, 'contracts/create.html', {
        'contractors': contractors,
        'consultants': consultants,
        'number': number,
        'name': name,
        'department_id': department_id,
        'amount': amount,
        'signing_date': signing_date,
        'site_handover_date': site_handover_date,
        'actual_start_date': actual_start_date,
        'duration': duration,
        'company_id': company_id
    })

# Edit Contract
@role_required('admin')
def contracts_edit(request, contract_id):
    contractors = Company.objects.filter(type='contractor')
    consultants = Company.objects.filter(type='consultant')

    contract = get_object_or_404(Contract, id=contract_id)

    number = contract.number
    name = contract.name
    department_id = contract.department_id
    amount = contract.amount
    signing_date = contract.signing_date
    site_handover_date = contract.site_handover_date
    actual_start_date = contract.actual_start_date
    duration = contract.duration
    company_id = contract.company_id

    if request.method == 'POST':
        number = request.POST.get('number', '').strip()
        name = request.POST.get('name', '').strip()
        department_id = request.POST.get('department_id', '').strip()
        amount = request.POST.get('amount', '').strip()
        signing_date = request.POST.get('signing_date', '').strip()
        site_handover_date = request.POST.get('site_handover_date', '').strip()
        actual_start_date = request.POST.get('actual_start_date', '').strip()
        duration = request.POST.get('duration', '').strip()
        company_id = request.POST.get('company_id', '').strip()

        contract.number = number
        contract.name = name
        contract.department_id = department_id
        contract.amount = amount
        contract.signing_date = signing_date
        contract.site_handover_date = site_handover_date
        contract.actual_start_date = actual_start_date
        contract.duration = duration
        contract.company_id = company_id
        contract.save()

        messages.success(request, f"تم تعديل العقد {contract.name} بنجاح")
        return redirect('contracts')

    return render(request, 'contracts/edit.html', {
        'contractors': contractors,
        'consultants': consultants,
        'contract': contract,
        'number': number,
        'name': name,
        'department_id': department_id,
        'amount': amount,
        'signing_date': signing_date,
        'site_handover_date': site_handover_date,
        'actual_start_date': actual_start_date,
        'duration': duration,
        'company_id': company_id
    })
