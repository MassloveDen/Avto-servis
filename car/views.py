
from django.shortcuts import render, redirect
from .models import Car, Color, Mark, Modl, New_Car
from .forms import CarForm

from django.views.generic import DetailView

# Create your views here.

def car_mark(request):

    marks = Mark.objects.all()
    avto = Car.objects.order_by('title')
    return render(request, "car/cars.html", {'marks': marks, 'avto': avto})





def char(request):
    colors = Color.objects.all()
    models = Modl.objects.all()
    # avto = Car.objects.order_by('title')
    avto = New_Car.objects.all()
    # sail = Sail.objects.all()
    return render(request, "car/char.html", {'colors': colors, 'models': models, 'avto': avto, })





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



# class CarDetailView(DetailView):
#     model = Car
#     template_name = 'car/car_detail.html'
#     context_object_name = 'car_detail'

class New_CarDetailView(DetailView):
    model = New_Car
    template_name = 'car/new.html'
    context_object_name = 'car_detail'