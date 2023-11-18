from django.http import HttpResponse
from django.shortcuts import render
# def  index(request):
#     return HttpResponse('''<h1> hello <h1><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">  Django tutu</a>''')
# def  about(request):
#     return HttpResponse("hello about")
def  index(request):
    params = {
        'name': 'Rutvik','place':'Surat'
    }
    return render (request, 'index.html',params)
def  analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    removespace = request.GET.get('removespace','off')
    print(removepunc)
    print(djtext)
    # analyzed = djtext
    if removepunc == 'on':  
        punctuations = '''!()-[]{};:'"\,<>.@#$%&*_~^'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed = analyzed + i
        params = {'purouse':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
                analyzed = analyzed + char.upper()
                
        params = {'purouse':'Change to upper case','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    elif(removespace=="on"):
        analyzed=""
        # punctuations = "  "
        # for char in djtext:

        #         if char != punctuations:
        #             analyzed = analyzed + char
        for index, char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1]==" "):
                analyzed = analyzed + char

                
        params = {'purouse':'remover new lines','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    else:
        return HttpResponse("Error")
def  capfirst(request):
    return HttpResponse("Captitalize first")