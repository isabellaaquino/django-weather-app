from django.contrib import admin
from django.urls import path
from .views import indexView


urlpatterns = [
    path('', indexView, name='home'),
]