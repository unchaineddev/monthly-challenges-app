from django.urls import path

from . import views

urlpatterns = [
    path("january", views.first_view)  # views.function_name
]