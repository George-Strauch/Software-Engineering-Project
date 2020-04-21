from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('hello')  # todo: this will pass html file for the home page


def posting_view(request):
    return HttpResponse('hello')  # todo: this will pass html file for the home page

