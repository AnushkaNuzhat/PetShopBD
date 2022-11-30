from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Forms and Model
from user.models import *
from user.forms import *
# Create your views here.


def signup_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created Succesfully!")
        else:
            messages.warning(
                request, "Could not create acoount! Please try again")
        return HttpResponseRedirect(reverse('user_app:login'))
    return render(request, 'store/register.html', context={'form': form})


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Succesfully!")
                return HttpResponseRedirect(reverse('home'))
    return render(request, 'store/login.html', context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out succesfully")
    return HttpResponseRedirect(reverse('home'))


@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile information saved")
            form = ProfileForm(instance=profile)
    return render(request, 'store/change_profile.html', context={'form': form})
