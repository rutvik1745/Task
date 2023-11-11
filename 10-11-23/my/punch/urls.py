from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('star', views.star, name='star'),
    path('end', views.end, name='end'),
    path('about/', views.about, name='about'),
]