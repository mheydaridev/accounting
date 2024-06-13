from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, CompanyRegisterForm, CompanyUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout as logout_utils
from .models import Company
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def company_register(request):
    if request.method == 'POST':
        company_register_form = UserRegisterForm(request.POST)
        if company_register_form.is_valid():
            user = company_register_form.save()
            login(request, user)
            messages.success(request, 'حساب کاربری شرکت با موفقیت ساخته شد.', 'success')
            return redirect('accounts:company_register_information')
    else:
        company_register_form = UserRegisterForm()
        context = {
            'company_register_form': company_register_form,
        }
    return render(request, 'accounts/company_register.html', context)


@login_required
def company_register_information(request):
    if request.method == 'POST':
        company_register_information_form = CompanyRegisterForm(request.POST)
        if company_register_information_form.is_valid():
            company = company_register_information_form.save(commit=False)
            company.user = request.user
            request.user.email = company_register_information_form.cleaned_data.get('email')
            request.user.save()
            company.save()
            messages.success(request, 'اطلاعات کاربری شرکت با موفقیت ثبت شد.', 'success')
            return redirect('accounts:profile')
    else:
        company_register_information_form = CompanyRegisterForm()
        context = {
            'company_register_information_form': company_register_information_form,
        }
    return render(request, 'accounts/company_register_information.html', context)


def login(request):
    if request.method == 'POST':
        authentication_form = AuthenticationForm(request, data=request.POST)
        if authentication_form.is_valid():
            username = authentication_form.cleaned_data.get('username')
            password = authentication_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'کاربر با موفقیت وارد شد.', 'success')
                company = get_object_or_404(Company, user=user)
                return redirect('accounts:profile', company_id=company.id)
            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.', 'error')
    else:
        authentication_form = AuthenticationForm()
        context = {
            'authentication_form': authentication_form,
        }
    return render(request, 'accounts/login.html', context)


def profile(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    context = {
        'company': company,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def update_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.method == 'POST':
        company_update_form = CompanyUpdateForm(request.POST, instance=company)
        if company_update_form.is_valid():
            company = company_update_form.save(commit=False)
            request.user.email = company_update_form.cleaned_data.get('email')
            request.user.save()
            company.save()
            messages.success(request, 'اطلاعات شرکت با موفقیت بروزرسانی شد.', 'success')
            return redirect('accounts:profile', company_id=company.id)
    else:
        company_update_form = CompanyUpdateForm(instance=company)        
        context = {
            'company_update_form': company_update_form,
        }
    return render(request, 'accounts/company_update.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'رمز عبور شما با موفقیت تغییر یافت.', 'success')
            return redirect('accounts:profile', company_id=request.user.company.id)
    else:
        password_change_form = PasswordChangeForm(request.user)
        context = {
            'password_change_form': password_change_form,
        }
    return render(request, 'accounts/change_password.html', context)


def logout(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    context = {
        'company': company,
    }
    if request.method == 'POST':
        logout_utils(request)
        messages.success(request, 'کاربر با موفقیت خارج شد.', 'success')
        return redirect('home')
    return render(request, 'accounts/logout.html', context)


@login_required
def delete_account(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    context = {
        'company': company,
    }
    if request.method == 'POST':
        user = company.user
        company.delete()
        user.delete()
        messages.success(request, 'حساب کاربری شما با موفقیت حذف شد.', 'success')
        return redirect('home')
    return render(request, 'accounts/delete_account.html', context)