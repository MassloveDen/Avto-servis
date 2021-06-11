
from django.shortcuts import render
from .models import Car, Color, Mark, Modl


# Create your views here.





def car_mark(request):

    marks = Mark.objects.all()
    avto = Car.objects.order_by('title')
    return render(request, "car/cars.html", {'marks': marks, 'avto': avto})

def char(request):
    colors = Color.objects.all()
    models = Modl.objects.all()
    avto = Car.objects.order_by('title')
    return render(request, "car/char.html", {'colors': colors, 'models': models, 'avto': avto})

