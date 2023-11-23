from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.IndexView.as_view(), name="BlogHome"),
    path("blogpost/<int:myid>",views.BlogPostView.as_view(),name='blogpost')
]
