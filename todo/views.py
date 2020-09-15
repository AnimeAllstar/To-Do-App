from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    items = TodoItem.objects.all()
    context = {
        'items': items
    }
    return render(request, 'home.html', context)


def addItem(request):
    newItem = TodoItem(content=request.POST['content'])
    newItem.save()
    return HttpResponseRedirect("/")

def deleteItem(request, itemId):
    temp = TodoItem.objects.get(id=itemId)
    temp.delete()
    return HttpResponseRedirect("/")
