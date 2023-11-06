from django.urls import path
from old import views

urlpatterns = [
    path("old/", views.ind, name="ind"),
]