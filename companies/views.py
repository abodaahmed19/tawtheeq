from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from helpers.utils import role_required
from .models import Company

# Companies
@role_required('admin')
def companies(request):
    companies = Company.objects.all()
    contractors = Company.objects.filter(type='contractor')
    consultants = Company.objects.filter(type='consultant')
    

    return render(request, 'companies/index.html', {
        'companies': companies,
        'contractors': contractors,
        'consultants': consultants
    })

# Create Company
@role_required('admin')
def companies_create(request):
    name = request.POST.get('name', '')
    cr_number = request.POST.get('cr_number', '')
    cr_expiry = request.POST.get('cr_expiry', '')
    phone = request.POST.get('phone', '')
    mobile = request.POST.get('mobile', '')
    email = request.POST.get('email', '')
    website = request.POST.get('website', '')
    address = request.POST.get('address', '')
    type = request.POST.get('type', '')
    if request.method == 'POST':
        name = request.POST.get('name')
        cr_number = request.POST.get('cr_number') or None
        cr_expiry = request.POST.get('cr_expiry') or None
        phone = request.POST.get('phone') or None
        mobile = request.POST.get('mobile') or None
        email = request.POST.get('email') or None
        website = request.POST.get('website') or None
        address = request.POST.get('address') or None
        type = request.POST.get('type') or None

        company = Company(name=name,cr_number=cr_number,cr_expiry=cr_expiry,phone=phone,mobile=mobile,email=email,website=website,address=address,type=type)
        company.save()
        messages.success(request, f"تم إنشاء المقاول أو الأستشاري {company.name} بنجاح")
        return redirect('companies')

    return render(request, 'companies/create.html', {
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

# Edit Company
@role_required('admin')
def companies_edit(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    name = company.name
    cr_number = company.cr_number
    cr_expiry = company.cr_expiry
    phone = company.phone
    mobile = company.mobile
    email = company.email
    website = company.website
    address = company.address
    type = company.type

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

        company.name = name
        company.cr_number = cr_number
        company.cr_expiry = cr_expiry
        company.phone = phone
        company.mobile = mobile
        company.email = email
        company.website = website
        company.address = address
        company.type = type
        company.save()

        messages.success(request, f"تم تعديل المقاول أو الأستشاري {company.name} بنجاح")
        return redirect('companies')

    return render(request, 'companies/edit.html', {
        'company': company,
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
