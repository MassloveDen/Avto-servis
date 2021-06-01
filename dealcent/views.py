from django.shortcuts import render




def index(request):
    data = {
        'title': 'Main page',
        'values': ['Some', 'hello', '123']
    }
    return render(request, "dealcent/home.html", data)

def servise(request):
    return render(request, "uslugi/servise.html")

def dil_list(request):
    return render(request, "dealcent/centers.html")

