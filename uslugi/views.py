from django.http import HttpResponse
from django.shortcuts import render

from .models import Sail, Uslugi, Repair


# Create your views here.





def servise(request):
    servise = Uslugi.objects.all()
    return render(request, 'uslugi/servise.html', {'servise': servise})

def scladavto(request):
    return render(request, "dealcent/scladavto.html")

def scladzp(request):
    return render(request, "dealcent/scladzp.html")

def sail(request):
    sail = Sail.objects.all()
    return render(request, "uslugi/sail.html", {'sail': sail})

def repair(request):
    repair = Repair.objects.all()
    return render(request, "uslugi/repair.html", {'repair': repair})
