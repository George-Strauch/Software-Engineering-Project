from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username} account created")
            return redirect('home')
    else:
        form = UserRegisterForm()

    # return render(request, 'users/register.html', {'form': form})     todo: create html file
    return HttpResponse()  #


def view_profile(request):
    # return render(request, 'users/profile.html', {'form': form})     todo: create html file
    return HttpResponse()  #


def edit_profile(request):
    # return render(request, 'users/edit_profile.html', {'form': form})     todo: create html file
    return HttpResponse()  #


def sign_in(request):
    # return render(request, 'users/sign_in.html', {'form': form})     todo: create html file
    return HttpResponse()  # todo
