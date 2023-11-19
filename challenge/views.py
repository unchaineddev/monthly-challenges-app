from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseNotFound  #for 404 pages

# Create your views here.

# first view
# def first_view(request):
#     return HttpResponse("Work out!")

# def second_view(request):
#     return HttpResponse("Eat Healthy!")


# def march(request):
#     return HttpResponse("Go for a Jog!")
    

def my_monthly_challenge(request, month):  # month is passed in url i.e  <month>
    text = None
    
    if month == 'january':
        text = "Work out!"
    elif month == 'february':
        text = "Eat Healthy!"
    elif month == 'march':
        text = "Go for a Walk!"
    elif month == 'april':
        text = "Play a sport!"
    elif month == 'may':
        text = "May the Job Search begin!"
    else:
        return HttpResponseNotFound("404 PAGE NOT FOUND!")

    return HttpResponse(text)