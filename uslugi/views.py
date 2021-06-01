from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def servise(request):
    return render(request, 'uslugi/servise.html')

def scladavto(request):
    return render(request, "dealcent/scladavto.html")

def scladzp(request):
    return render(request, "dealcent/scladzp.html")

def sail(request):
    return render(request, "uslugi/sail.html")

def repair(request):
    return render(request, "uslugi/repair.html")
