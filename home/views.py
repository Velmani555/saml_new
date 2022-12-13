from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<b>I am Velmani!!!!!!!<b>")


def contactus(request):
    return HttpResponse("hi")
# Create your views here.
