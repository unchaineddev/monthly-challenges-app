from django.http import HttpResponse, response
from django.shortcuts import redirect, render
from django.http import HttpResponseNotFound # 404 pages
from django.http import HttpResponseRedirect  # redirect links

from django.urls import reverse # reverse function


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


def my_local_host(request):
    list_items = ""
    all_months =  list(challenges.keys())

    for month in all_months:
        month_path = reverse("my-challenge", args=[month])  # reverse function
        list_items += f'<li><ul><a href="{month_path}">{month.capitalize()}</a></ul></li>'

    response_data = f'<ul>{list_items}</ul>'
    
    return HttpResponse(response_data)


def my_monthly_challenge_number(request, month):
    all_months =  list(challenges.keys())
    if month > len(all_months):
        return HttpResponseNotFound("Invalid! try again!")

    forward_month = all_months[month - 1]  # -1 because index starts with 0 
    redirect_path = reverse("my-challenge", args=[forward_month])  # reverse function
    # return HttpResponseRedirect("/challenge/" + forward_month)  # redirect links
    return HttpResponseRedirect(redirect_path)

def my_monthly_challenge(request, month):  # month is passed in url i.e  <month>

    try:
        final_text = challenges[month] # accessing the key
        response_data = f"<h1>{final_text}</h1>"
        return HttpResponse(response_data)
        # return HttpResponse(final_text)
    except:
        return HttpResponseNotFound("<h1>404 NOT FOUND!</h1>")
