from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from helpers.utils import role_required
from .models import Department
from .models import Agent
from django.http import JsonResponse

# Departments
@role_required('admin')
def departments(request):
    departments = Department.objects.all()
    main_departments = departments.filter(parent__isnull=True)
    sub_departments = departments.filter(parent__isnull=False)

    return render(request, 'departments/index.html', {
        'departments': departments,
        'main_departments': main_departments,
        'sub_departments': sub_departments
    })

# Create Department
@role_required('admin')
def departments_create(request):
    agents = Agent.objects.all()
    name = request.POST.get('name', '')
    agent_id = request.POST.get('agent_id', '')
    if request.method == 'POST':
        name = request.POST.get('name')
        agent_id = request.POST.get('agent_id')
        parent_id = request.POST.get('parent_id')

        department = Department(name=name,agent_id=agent_id,parent_id=parent_id)
        department.save()
        messages.success(request, f"تم إنشاء الإدارة {department.name} بنجاح")
        return redirect('departments')

    return render(request, 'departments/create.html', {
        'agents': agents,
        'name': name,
        'agent_id': agent_id
    })

# Edit Department
@role_required('admin')
def departments_edit(request, department_id):
    department = get_object_or_404(Department, id=department_id)

    name = department.name

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()

        department.name = name
        department.save()

        messages.success(request, f"تم تعديل الإدارة {department.name} بنجاح")
        return redirect('departments')

    return render(request, 'departments/edit.html', {
        'department': department,
        'name': name,
    })

# Get Department By Id
def departments_by_parent(request):
    parent_id = request.GET.get('parent_id')

    if parent_id:
        departments = Department.objects.filter(parent_id=parent_id)
    else:
        departments = Department.objects.filter(parent__isnull=True)

    data = departments.values('id', 'name')
    return JsonResponse(list(data), safe=False)