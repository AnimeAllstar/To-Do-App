from django.shortcuts import render
from django.http import HttpResponseRedirect
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
def addList(request):
    if request.method == 'POST':
        newList = TodoList(title=request.POST['title'], creator=request.user)
        newList.save()
    return HttpResponseRedirect("/")


@login_required
def deleteList(request, itemId):
    temp = TodoList.objects.get(id=itemId)
    temp.delete()
    return HttpResponseRedirect("/")
