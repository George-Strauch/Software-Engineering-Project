from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    context = {
        'properties': Property.objects.all()
    }
    return render(request, 'rentals/home.html', context=context)  # todo


def property_view(request):
    return HttpResponse('hello')  # todo


def rent_property(request):
    return HttpResponse('hello')  # todo


def create_posting(request):
    return HttpResponse('hello')  # todo


def give_feedback(request):
    return HttpResponse('hello')  # todo


def edit_reservation(request):
    return HttpResponse('hello')  # todo



