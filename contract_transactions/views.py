from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from helpers.utils import role_required
from .models import ContractTransaction
from companies.models import Company

# Contract Transactions
@role_required('admin')
def contract_transactions(request):
    contract_transactions = ContractTransaction.objects.all()
    not_complated_transactions = ContractTransaction.objects.filter(is_documented=False)
    complated_transactions = ContractTransaction.objects.filter(is_documented=False)
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

# Edit Contract Transaction
@role_required('admin')
def contract_transactions_edit(request, contract_transaction_id):
    contract_transaction = get_object_or_404(Contract, id=contract_transaction_id)

    name = contract_transaction.name
    cr_number = contract_transaction.cr_number
    cr_expiry = contract_transaction.cr_expiry
    phone = contract_transaction.phone
    mobile = contract_transaction.mobile
    email = contract_transaction.email
    website = contract_transaction.website
    address = contract_transaction.address
    type = contract_transaction.type

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
