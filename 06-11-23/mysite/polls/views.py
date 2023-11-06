from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render


def index(request):
    return HttpResponse("helllo ")