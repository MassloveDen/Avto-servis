from django.contrib import admin

# Register your models here.
from .models import Mark, Modl, Color, Car, New_Car

admin.site.register(Car)
admin.site.register(Mark)
admin.site.register(Modl)
admin.site.register(Color)
admin.site.register(New_Car)