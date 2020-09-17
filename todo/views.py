from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
from django.contrib.auth.decorators import login_required


@login_required
def todoView(request):
    items = TodoItem.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/home.html', context)


@login_required
def addItem(request):
    newItem = TodoItem(content=request.POST['content'])
    newItem.save()
    return HttpResponseRedirect("/")


@login_required
def deleteItem(request, itemId):
    temp = TodoItem.objects.get(id=itemId)
    temp.delete()
    return HttpResponseRedirect("/")
