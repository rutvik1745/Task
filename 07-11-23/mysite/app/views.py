# from django.shortcuts import render
from django.http import HttpResponse
from app.models import Profile
from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls")
    # latest_question_list = Profile.objects.filter()
    # output = ", ".join([q.first_name for q in latest_question_list])
    # return HttpResponse(output)
    

    latest_question_list = Profile.objects.filter()
    context = {"latest_question_list": latest_question_list}
    return render(request, "app/Home.html", context)

def detail(request, p_id):
    return HttpResponse("You're id %s." % p_id )