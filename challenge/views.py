from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseNotFound


challenges = {
    'january': "Work out!",
    'february': "Eat Healthy!",
    'march': "Go for a Walk!",
    'april': "Play a sport!",
    'may': "May the Job Search begin!",
    'june': "Deploy an app!",
    'july': "Solve problems everyday!",
    'august': "Read a book!",
    'september': "Sleep for 8 hours",
    'october': "Travel to a new place!",
    'november': "Learn something new!",
    'december': "Relax for 15 mins!"
}

# Create your views here.

# first view
# def first_view(request):
#     return HttpResponse("Work out!")

# def second_view(request):
#     return HttpResponse("Eat Healthy!")


# def march(request):
#     return HttpResponse("Go for a Jog!")

def my_monthly_challenge_number(request, month):
    return HttpResponse(month)
  

def my_monthly_challenge(request, month):  # month is passed in url i.e  <month>

    try:
        final_text = challenges[month]
        return HttpResponse(final_text)
    except:
        return HttpResponseNotFound("404 NOT FOUND!")
