from django.urls import path
from django import forms
from app import views

urlpatterns = [
    path("",views.Index.as_view(),name="index"),
    path("login/",views.LoginView.as_view(), name='login'),
    # path("profile",views, name='profile')
    path("login/profile",views.Index.as_view(),name="profile"),
    path('register/', views.RegistrationView.as_view(), name='registation'),
    path("register/profile",views.Index.as_view(),name="register"),
    path("logout",views.Index.as_view(),name="logout"),
    # path("profile",views.Profile.as_view(),name="profile"),
    path("star",views.StarTimeView.as_view(), name='star'),

]