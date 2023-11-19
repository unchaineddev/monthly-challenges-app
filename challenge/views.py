from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# first view
def first_view(request):
    return HttpResponse("Work out!")

def second_view(request):
    return HttpResponse("Eat Healthy!")