from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, new_profile_id):
    response = "You're looking at the results of question %s."

    return HttpResponse(response % new_profile_id)