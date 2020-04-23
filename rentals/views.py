from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    context = {
        'properties': Property.objects.all()
    }
    return HttpResponse()  # todo


def property_view(request):
    return HttpResponse()  # todo


def rent_property(request):
    return HttpResponse()  # todo


def create_posting(request):
    return HttpResponse()  # todo


def give_feedback(request):
    return HttpResponse()  # todo


def edit_reservation(request):
    return HttpResponse()  # todo



