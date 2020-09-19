from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import TodoList, TodoItem
from .forms import ListCreateForm, ItemCreateForm


@login_required
def todoView(request):
    if request.method == 'POST':
        if 'add_item' in request.POST:
            item_form = ItemCreateForm(request.user, request.POST)
            if item_form.is_valid():
                item_form.save()
                return redirect('todo-home')
        elif 'create_list' in request.POST:
            list_form = ListCreateForm(request.POST)
            if list_form.is_valid():
                temp_list = list_form.save(commit=False)
                temp_list.creator = User.objects.get(
                    username=request.user)
                temp_list.save()
                return redirect('todo-home')
    else:
        list_form = ListCreateForm()
        item_form = ItemCreateForm(request.user)
    lists = TodoList.objects.all().filter(creator=request.user)
    context = {
        'lists': lists,
        'list_form': list_form,
        'item_form': item_form,
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
