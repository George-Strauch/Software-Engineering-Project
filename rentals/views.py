from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import *
from user.forms import AddressForm


def home(request):
    context = {
        'properties': Property.objects.all()
    }
    return render(request, 'rentals/home.html', context=context)  # todo



@login_required
def view_property(request, prop_pk):
    context = {
        'property': Property.objects.get(pk=prop_pk)
    }
    return render(request, 'rentals/property.html', context=context)




@login_required
def rent_property(request, property_pk):
    p = Property.objects.get(pk=property_pk)

    if request.user == p.posted_by:
        messages.error(request, 'you cannot rent your own property')
        return redirect('prop-detail', property_pk)


    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            r = form.save()
            messages.success(request, f"{r}")
            return redirect('prop-detail', property_pk)
        else:
            print('failed')
            messages.error(request, f"could not make reservation")
            form = ReservationForm(request.POST)
    else:
        form = ReservationForm()

    context = {
        'form': form,
    }
    return render(request, 'rentals/create_property_posting.html', context=context)



@login_required
def create_property(request):
    if not request.user.userprofile.is_landlord:
        messages.error(request, "you cant do that")
        return redirect('rentals-home')
    else:
        if request.method == 'POST':
            form = PropertyForm(request.POST, request.FILES)
            address_form = AddressForm(request.POST)

            if form.is_valid() and address_form.is_valid():
                p = form.save()
                a = address_form.save()
                p.address = a
                p.posted_by = request.user.userprofile
                p.save()
                print(f'created property: {p}')
                messages.success(request, f"{p}")
                return redirect('prop-detail', p.pk)

            else:
                messages.error(request, f" could not create property")
                print(f'there was a problem... af{address_form.is_valid()},   form:{form.is_valid()}')
                return redirect('prop-create')

        else:
            form = PropertyForm()
            address_form = AddressForm()

    context = {
        'form': form,
        'address_form': address_form
    }
    return render(request, 'rentals/create_property_posting.html', context=context)



@login_required
def give_feedback(request, reservation_pk):
    return HttpResponse('hello')  # todo


@login_required
def edit_reservation(request):
    return HttpResponse('hello')  # todo


