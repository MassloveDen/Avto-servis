from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.servise),
    path('sail', views.sail),
    path('repair', views.repair),
    path('scladzp', views.scladzp),
    path('scladavto', views.scladavto),

]