from django.urls import path

from app import views

urlpatterns = [
    path("",views.index,name='index'),
    path("<int:p_id>/", views.detail, name="detail"),

]