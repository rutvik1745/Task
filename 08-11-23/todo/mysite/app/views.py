
from django.shortcuts import render, redirect
from django.contrib import messages
 
from .forms import TodoForm
from .models import Todo
 


def index(request):
    item_list  = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        form = TodoForm()
        print(item_list)
        page = {
            "forms": form,
            "list": item_list,
            "title": "TODO LIST",
            
        }
    return render(request, 'index.html')
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    print(item)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')

def remove1(request):
    item = Todo.objects.all()
    print(item)
    return render(request, 'first.html',{'item':item})
