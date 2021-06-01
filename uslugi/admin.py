from django.contrib import admin

# Register your models here.
from .models import Sail, Repair, Zapas, SkladZap, SkladAvto, Uslugi

admin.site.register(Sail)
admin.site.register(Repair)
admin.site.register(Zapas)
admin.site.register(SkladZap)
admin.site.register(SkladAvto)
admin.site.register(Uslugi)

