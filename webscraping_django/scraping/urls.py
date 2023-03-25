from django.urls import path
from . import views

urlpatterns = [
    path('first/',views.trial),
    path('',views.home),
]


