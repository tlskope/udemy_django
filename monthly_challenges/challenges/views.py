from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("Eat no meat for the month")

def february():
    return HttpResponse("Walk for at least 20 minutes every day")