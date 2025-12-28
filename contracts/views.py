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
    contract = get_object_or_404(Contract, id=contract_id)

    name = contract.name
    cr_number = contract.cr_number
    cr_expiry = contract.cr_expiry
    phone = contract.phone
    mobile = contract.mobile
    email = contract.email
    website = contract.website
    address = contract.address
    type = contract.type

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        cr_number = request.POST.get('cr_number', '').strip()
        cr_expiry = request.POST.get('cr_expiry', '').strip()
        phone = request.POST.get('phone', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        email = request.POST.get('email', '').strip()
        website = request.POST.get('website', '').strip()
        address = request.POST.get('address', '').strip()
        type = request.POST.get('type', '').strip()

        contract.name = name
        contract.cr_number = cr_number
        contract.cr_expiry = cr_expiry
        contract.phone = phone
        contract.mobile = mobile
        contract.email = email
        contract.website = website
        contract.address = address
        contract.type = type
        contract.save()

        messages.success(request, f"تم تعديل العقد {contract.name} بنجاح")
        return redirect('contracts')

    return render(request, 'contracts/edit.html', {
        'contract': contract,
        'name': name,
        'cr_number': cr_number,
        'cr_expiry': cr_expiry,
        'phone': phone,
        'mobile': mobile,
        'email': email,
        'website': website,
        'address': address,
        'type': type
    })
