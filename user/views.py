from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *


def register_user(request):
    if request.method == 'POST':
        u_form = MakeUserForm(request.POST)
        p_form = MakeProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            username = u_form.cleaned_data.get('username')
            messages.success(request, f"{username} account created")
            return redirect('home')
    else:
        u_form = MakeUserForm()
        p_form = MakeProfileForm()

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/register.html', context=context)


@login_required
def view_profile(request):
    comtext = {
        'user': request.user,
    }    # return render(request, 'users/profile.html', {'form': form})     todo: create html file
    return HttpResponse('hello')  #


#
# @login_required
# def edit_profile(request):
#     if request == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = UpdateProfileForm(request.POST, instance=request.user)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f"success")
#             return redirect('home')
#         else:
#             messages.success(request, "failed, not saved")
#
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = UpdateProfileForm(instance=request.user)
#
#     comtext = {
#         'u_form': u_form,
#         'p_form': p_form,
#     }

    # return render(request, 'users/edit_profile.html', context)     todo: create html file
    return HttpResponse('hello')  #


def sign_in(request):
    comtext = {
        'user': request.user,
    }
    # return render(request, 'users/sign_in.html', {'form': form})     todo: create html file
    return HttpResponse('hello')  # todo
