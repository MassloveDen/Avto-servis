from django.urls import path
from . import views


urlpatterns = [
    path('', views.car_mark, name='cars'),
    path('char', views.char, name='char'),
    path('create_car', views.create_car, name='create_car'),
    # path('<int:pk>', views.CarDetailView.as_view(), name='car_detail'),
    path('<int:pk>', views.New_CarDetailView.as_view(), name='car_detail')
    ,
]