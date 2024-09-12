from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return HttpResponse('<h1 style="color: red; text-align: center"";>Hola Mundo Django</h1>')
# Create your views here.
