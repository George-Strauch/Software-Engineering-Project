from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *


def register_user(request):
    print(request.method)
    if request.method == 'POST':
        u_form = MakeUserForm(request.POST)
        p_form = MakeProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            u = u_form.save()

            # prof = UserProfile.objects.create(user=u, is_landlord=p_form.cleaned_data.get('boolf'))
            u.userprofile.is_landlord = p_form.cleaned_data.get('property_owner')
            u.userprofile.save()
            u.save()

            print(u.userprofile)
            username = u.username
            print(f'{username} created... {u.userprofile}')
            messages.success(request, f"{username} account created")
            return redirect('rentals-home')
        else:
            print("there was a problem")
            print(f'uform: {u_form.is_valid()}, pfrom: {p_form.is_valid()}')
            messages.error(request, f"account not created, there was a problem... try using a different username")
            return redirect('register')

    u_form = MakeUserForm()
    p_form = MakeProfileForm()
    address_form = AddressForm()

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'address_form': address_form
    }
    return render(request, 'users/register.html', context=context)



@login_required
def view_profile(request):
    comtext = {
        'user': request.user,
    }    # return render(request, 'users/profile.html', {'form': form})     todo: create html file
    return HttpResponse('hello')  #



def sign_in(request):
    return render(request, 'users/signin.html')




@login_required
def edit_profile(request):
    print(request.method)
    if request.method == 'POST':
        u_form = EditUserForm(request.POST, instance=request.user)
        pfp_form = PfpForm(request.POST, request.FILES, instance=request.user.userprofile)
        p_form = EditProfileForm(request.POST, instance=request.user.userprofile)
        a_form = AddressForm(request.POST, instance=request.user.userprofile.address)

        if u_form.is_valid() and p_form.is_valid() and a_form.is_valid() and pfp_form.is_valid():
            a_form.save()
            pfp_form.save()
            p_form.save()
            u_form.save()

            messages.success(request, f"success")
            print('changes made')
            return redirect('rentals-home')
        else:
            messages.success(request, "failed, not saved")
            print('changes not made')
            return redirect('rentals-home')

    else:
        u_form = EditUserForm(instance=request.user)
        p_form = EditProfileForm(instance=request.user.userprofile)
        a_form = AddressForm(instance=request.user.userprofile.address)
        pfp_form = PfpForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'a_form': a_form,
        'pfp_form': pfp_form,
    }
    return render(request, 'users/edit_user.html', context)
