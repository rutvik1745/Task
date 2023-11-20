from django.http import HttpResponse
from django.shortcuts import render

def  index(request):
    params = {
        'name': 'Rutvik','place':'Surat'
    }
    return render (request, 'index.html',params)
def  analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    removespace = request.POST.get('removespace','off')
    print(removepunc)
    if removepunc == 'on':  
        punctuations = '''!()-[]{};:'"\,<>.@#$%&*_~^'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed = analyzed + i
        params = {'purouse':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:   
            analyzed = analyzed + char.upper()
                
        params = {'purouse':'Change to upper case','analyzed_text':analyzed}
        djtext = analyzed
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
                if char !="\n" and char !="\r":
                    analyzed = analyzed + char
                
        params = {'purouse':'Remove NewLine','analyzed_text':analyzed}
        djtext = analyzed
    if(removespace=="on"):
        analyzed=""
      
        for index, char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purouse':'remover Wide Space','analyzed_text':analyzed}
     
    if (removepunc != "on" and newlineremover != "on" and removepunc != "on" and fullcaps != "on"):
        return HttpResponse("Please select any operater")
    return render(request,"analyze.html",params)
def  capfirst(request):
    return HttpResponse("Captitalize first")