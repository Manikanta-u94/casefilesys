
from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('calender/', calender, name="calender"),
    path('all_cases/', all_cases, name="all_cases"),
]