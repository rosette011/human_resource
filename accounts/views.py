from django.shortcuts import (
    render,
    redirect
)
from .forms import (
    LoginForm,
    RegistrationForm,
    UpdateProfileForm,
    ChangePasswordForm
)
from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

import pdb

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('human_resource:home')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts:login')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)

@login_required
def profile_view(request):
    args = {'user': request.user}
    # pdb.set_trace()
    return render(request, 'accounts/profile.html', args)

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile_view')
    else:
        form = UpdateProfileForm(instance=request.user)
        context = {'form': form}
        return render(request, 'accounts/profile-edit.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile_view')

    else:
        form = ChangePasswordForm(request.user)

    return render(request, 'accounts/change-password.html', {'form': form})