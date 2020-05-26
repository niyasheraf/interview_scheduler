from django.urls import path
from main.views import register, time_slots
urlpatterns = [
    path('register/', register),
    path('slots/', time_slots),
]
