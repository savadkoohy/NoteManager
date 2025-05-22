from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms

# -------------------------------------------------------------------------------------------------------------

def media_admin(request):
    return {'media_url':settings.MEDIA_URL,}

def index(request):
    return render(request, "main-apps/index.html")

# ___________________________________________________________________________________________________________________________________________

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'ثبت‌نام موفقیت‌آمیز بود! خوش آمدید.')
            return redirect('notes:note_list')  # بعد از ثبت‌نام به لیست یادداشت‌ها می‌ریم
        else:
            messages.error(request, 'لطفا فرم را به درستی پر کنید.')
    else:
        form = SignUpForm()
    return render(request, 'main-apps/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'خوش آمدید، {user.username}!')
            return redirect('notes:note_list')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
    else:
        form = AuthenticationForm()
    return render(request, 'main-apps/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'شما با موفقیت خارج شدید.')
    return redirect('login')

# -------------------------------------------------------------------------------------------------

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "پروفایل با موفقیت به‌روزرسانی شد.")
            return redirect('main:edit_profile')
    else:
        form = EditProfileForm(instance=request.user)
    
    return render(request, 'main-apps/edit_profile.html', {'form': form})


