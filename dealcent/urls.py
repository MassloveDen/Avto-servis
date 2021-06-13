from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('uslugs', views.servise, name='uslugi'),
    path('centers', views.dil_list, name='centers'),
    path('<int:pk>', views.CentDetailView.as_view(), name='cent_detail')
    # path('', include('uslugi.urls')),
    # path('cars', views.cars, name='cars'),
    # path('scladavto', views.scladavto, name='scladavto'),
    # path('scladzp', views.scladzp, name='scladzp'),
]
