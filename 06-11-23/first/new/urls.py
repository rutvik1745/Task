from django.urls import path
from new import views

urlpatterns = [
    path("", views.index,name='index'),
    path("detail/",views.detail,name='detail')
    
]