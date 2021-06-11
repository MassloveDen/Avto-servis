
from django.shortcuts import render, redirect
from .models import Car, Color, Mark, Modl
from .forms import CarForm


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

def create_car(request):
    error = ''
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('uslugi')
        else:
            error = 'Неверная конфигурация'

    form = CarForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, "car/create.html", data)

# def learn_create(request):
#     form = CarForm()
#     data = {
#         'form': form
#     }
#     return render(request, "car/create.html", data)