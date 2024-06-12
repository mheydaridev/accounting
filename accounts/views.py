# from django.shortcuts import render, redirect
# from .forms import CustomUserRegisterForm, CustomUserUpdateForm, CustomUserLoginForm
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout

# # Create your views here.
# def user_register(request):
#     if request.method == 'POST':
#         custom_user_register_form = CustomUserRegisterForm(request.POST)
#         if custom_user_register_form.is_valid():
#             user = custom_user_register_form.save()
#             login(request, user)
#             messages.success(request, 'کاربر با موفقیت ثبت نام شد.', 'success')
#             return redirect('home')
#     else:
#         custom_user_register_form = CustomUserRegisterForm()
#         context = {
#             'custom_user_register_form': custom_user_register_form,
#         }
#     return render(request, 'accounts/user_register.html', context)


# def user_login(request):
#     if request.method == 'POST':
#         custom_user_login_form = CustomUserLoginForm(request.POST)
#         if custom_user_login_form.is_valid():
#             username = custom_user_login_form.cleaned_data.get('username')
#             password = custom_user_login_form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'کاربر با موفقیت وارد شد.', 'success')
#                 return redirect('home')
#             else:
#                 messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.', 'error')
#     else:
#         custom_user_login_form = CustomUserLoginForm()
#         context = {
#             'custom_user_login_form': custom_user_login_form,
#         }
#     return render(request, 'accounts/user_login.html', context)


# def user_detail(request):
#     return render(request, 'accounts/user_detail.html')


# def update_user(request):
#     if request.method == 'POST':
#         custom_user_update_form = CustomUserUpdateForm(request.POST, instance=request.user)
#         if custom_user_update_form.is_valid():
#             custom_user_update_form.save()
#             messages.success(request, 'اظلاعات کاربر با موفقیت بروزرسانی شد.', 'success')
#             return redirect('accounts:user_detail')
#     else:
#         custom_user_update_form = CustomUserUpdateForm(instance=request.user)
#         context = {
#             'custom_user_update_form': custom_user_update_form,
#         }
#     return render(request, 'accounts/update_user.html', context)


# def user_logout(request):
#     logout(request)
#     messages.success(request, 'کاربر با موفقیت خارج شد.', 'success')
#     return redirect('home')
