from django.contrib import admin
from django.urls import path, include

from encore import views

urlpatterns = [
    path('', views.index),
]