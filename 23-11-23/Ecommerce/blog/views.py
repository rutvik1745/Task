from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blogpost
from django.views import View

# Create your views here.
class IndexView(View):
    def get(self,request):
        myposts = Blogpost.objects.all()
        print(myposts)
        return render (request, 'blog/index.html',{'myposts':myposts})

class BlogPostView(View):
    def get(self,request,myid):
        post = Blogpost.objects.filter(post_id = myid)[0]
        print(post)
        return render(request, 'blog/blogpost.html',{'post':post})

