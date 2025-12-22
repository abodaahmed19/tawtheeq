from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from helpers.utils import role_required

# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة")
    return render(request, 'login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Home
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

# Users
User = get_user_model()

@role_required('admin')
def users(request):
    users = User.objects.all()
    admin = User.objects.filter(role='admin')
    manager = User.objects.filter(role='manager')
    company = User.objects.filter(role='company')
    reviewer = User.objects.filter(role='reviewer')
    user = User.objects.filter(role='user')

    return render(request, 'users/index.html', {
        'users': users,
        'admin': admin,
        'manager': manager,
        'company': company,
        'reviewer': reviewer,
        'user': user,
    })

# Create User
@role_required('admin')
def users_create(request):
    username = request.POST.get('username', '')
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    role = request.POST.get('role', '')
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        is_staff = False
        is_active = True

        if password != password_confirm:
            messages.error(request, "كلمتا المرور غير متطابقتين")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود بالفعل")
        else:
            user = User(username=username, name=name, email=email, role=role, is_staff=is_staff, is_active=is_active)
            user.set_password(password)
            user.save()
            messages.success(request, f"تم إنشاء المستخدم {user.username} بنجاح")
            return redirect('users')

    return render(request, 'users/create.html', {
        'username': username,
        'name': name,
        'email': email,
        'role': role
    })

# Edit User
@role_required('admin')
def users_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)

    username = user.username
    name = user.name
    email = user.email
    role = user.role

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        role = request.POST.get('role', '')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if User.objects.exclude(id=user.id).filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود بالفعل")
        elif password:
            if password != password_confirm:
                messages.error(request, "كلمتا المرور غير متطابقتين")
            else:
                user.set_password(password)
        else:
            user.username = username
            user.name = name
            user.email = email
            user.role = role
            user.save()

            messages.success(request, f"تم تعديل المستخدم {user.username} بنجاح")
            return redirect('users')

    return render(request, 'users/edit.html', {
        'user': user,
        'username': username,
        'name': name,
        'email': email,
        'role': role
    })
