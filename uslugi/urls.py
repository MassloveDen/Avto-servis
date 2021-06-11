from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.servise),
    path('sail', views.sail, name='price'),
    path('repair', views.repair, name= 'repair'),
    path('scladzp', views.scladzp),
    path('scladavto', views.scladavto, name='scladavto'),

]