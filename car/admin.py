from django.contrib import admin

# Register your models here.
from .models import Mark, Modl, Color, Car

admin.site.register(Car)
admin.site.register(Mark)
admin.site.register(Modl)
admin.site.register(Color)