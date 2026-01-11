from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={'name': 'Exemplo',})


def contato(request):
    return HttpResponse('contato 1')


def sobre(request):
    return HttpResponse('sobre 1')