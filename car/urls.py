from django.urls import path
from . import views


urlpatterns = [
    path('', views.car_mark, name='cars'),
    path('char', views.char, name='char'),
    # path('', views.avto, name='cars'),
]