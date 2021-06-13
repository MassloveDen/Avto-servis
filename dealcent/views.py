from django.shortcuts import render
from django.views.generic import DetailView

from .models import DealCent



def home(request):
    data = {
        'title': 'Главная страница дилера (Имя пользователя?)',
        'values': ['Some', 'hello', '123']
    }
    return render(request, "dealcent/home.html", data)

def servise(request):
    return render(request, "uslugi/servise.html")

def dil_list(request):
    cent = DealCent.objects.all()
    return render(request, "dealcent/centers.html", {'list': cent})

class CentDetailView(DetailView):
    model = DealCent
    template_name = 'dealcent/cent_detail.html'
    context_object_name = 'cent_detail'