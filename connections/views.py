from django.shortcuts import render


def connectionView(request):
    return render(request, 'connections/main.html')
