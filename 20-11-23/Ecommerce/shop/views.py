from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    detailsall = Product.objects.all()
    params={
        'details':detailsall}
    return render(request,'shop/index.html',params)

def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productview(request):
    return HttpResponse("We are at productview")

def checkout(request):
    return HttpResponse("We are at checkout")