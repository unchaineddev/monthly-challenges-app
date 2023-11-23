from django.urls import path

from . import views

urlpatterns = [
    # path("january", views.first_view),  # views.function_name
    # path("february", views.second_view),
    # path("march", views.march),

    # irrespective of what url we pass this will trigger
    path("", views.my_local_host),   # localhost
    path("<int:month>", views.my_monthly_challenge_number), # check if its integer first
    # path("<str:month>", views.my_monthly_challenge)   # str:month --> passed as a string
    path("<str:month>", views.my_monthly_challenge, name="my-challenge") # reverse function
]

