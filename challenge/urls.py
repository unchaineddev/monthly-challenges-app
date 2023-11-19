from django.urls import path

from . import views

urlpatterns = [
    # path("january", views.first_view),  # views.function_name
    # path("february", views.second_view),
    # path("march", views.march),
    path("<month>", views.my_monthly_challenge )  # irrespective of what url we pass this will trigger
]