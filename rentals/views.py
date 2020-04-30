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
def rent_property(request, prop_pk):
    p = Property.objects.get(pk=prop_pk)

    if request.user == p.posted_by:
        messages.error(request, 'you cannot rent your own property')
        return redirect('prop-detail', prop_pk)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            r = Reservation.objects.create(
                renter=request.user,
                property=p,
                start_date=form.cleaned_data.get('start_date'),
                end_date=form.cleaned_data.get('end_date')
            )

            messages.success(request, f"{r.property.address.street_address} booked")
            return redirect('prop-detail', prop_pk)
        else:
            print('failed')
            messages.error(request, f"could not make reservation")
            form = ReservationForm(request.POST)
    else:
        form = ReservationForm()

    context = {
        'form': form,
    }
    return render(request, 'rentals/rent_property.html', context=context)



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
                a = address_form.save()

                p = Property.objects.create(address=a,
                                            posted_by=request.user.userprofile,
                                            price_per_day=form.cleaned_data.get('price_per_day'),
                                            property_description=form.cleaned_data.get('property_description'),
                                            thumbnail=form.cleaned_data.get('thumbnail'),
                                            )

                # f.address.street_address = a.street_address
                # f.address.country = a.country
                # f.address.city = a.city
                # f.address.zip_code = a.zip_code
                # f.address.state = a.state
                #
                #
                # f.address.save()
                # f.save()
                # p = f


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
def my_listings(request):
    l = Property.objects.filter(posted_by=request.user.userprofile)
    print(l)
    context = {
        'listings': l
    }
    return render(request, 'rentals/property_list.html', context=context)




@login_required
def edit_listing(request, listing_pk):
    p = Property.objects.get(pk=listing_pk)

    if request.method == 'POST':
        prop = PropertyForm(request.POST, request.FILES)
        adr = AddressForm(request.POST)
        if prop.is_valid() and adr.is_valid():

            p.address.street_address = adr.cleaned_data['street_address']
            p.address.country = adr.cleaned_data['country']
            p.address.city = adr.cleaned_data['city']
            p.address.zip_code = adr.cleaned_data['zip_code']
            p.address.state = adr.cleaned_data['state']
            p.address.save()
            p.save()


            p.price_per_day = prop.cleaned_data.get('price_per_day')
            p.property_description = prop.cleaned_data.get('property_description')
            p.save()
            p.thumbnail = prop.cleaned_data.get('thumbnail')
            p.save()


            messages.success(request, f"saved")
            return redirect('prop-detail', listing_pk)
        else:
            print('failed')
            messages.error(request, f"could not make reservation")
            return redirect('prop-detail', listing_pk)
    else:
        prop = PropertyForm(instance=p)
        adr = AddressForm(instance=p.address)
        context = {
            'form': prop,
            'address': adr,
        }
        return render(request, 'rentals/edit_listing.html', context=context)


@login_required
def give_feedback(request, reservation_pk):
    return HttpResponse('hello')  # todo


@login_required
def edit_reservation(request):
    return HttpResponse('hello')  # todo


