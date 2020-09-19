from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import TodoList, TodoItem


@login_required
def todoView(request):
    lists = TodoList.objects.all().filter(creator=request.user)
    context = {
        'lists': lists,
    }
    return render(request, 'todo/home.html', context)


@login_required
def addItem(request):
    if request.method == 'POST':
        newItem = TodoItem(content=request.POST['content'], user=request.user)
        newItem.save()
    return HttpResponseRedirect("/")


@login_required
def deleteItem(request, itemId):
    temp = TodoItem.objects.get(id=itemId)
    temp.delete()
    return HttpResponseRedirect("/")
