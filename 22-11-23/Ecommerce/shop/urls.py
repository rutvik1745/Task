from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.IndexView.as_view(), name="ShopHome"),
    path("about/",views.about, name="AboutUs"),
    path("contact/",views.ContactView.as_view(), name="ContactUs"),
    path("tracker/",views.tracker, name="TrackingStatus"),
    path("search/",views.search, name="Search"),
    path("products/<int:myid>",views.ProductView.as_view(), name="ProductView"),
    path("checkout/",views.CheckoutView.as_view(), name="Checkout"),
]
