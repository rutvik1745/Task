from django.contrib import admin
from django.urls import path
from polls import views
# app_name = "polls"

urlpatterns = [
    path("", views.index, name='home')
]