from .models import Car
from django.forms import ModelForm, TextInput, ChoiceField

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'vin', 'mark', 'modl', 'color']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control'

            })
        }
        #     'mark': TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Марка'
        #     }),
        #     'modl': TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Модель'
        #     }),
        #     'color': TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Цвет'
        #     })
        # }

# class CarForm(ModelForm):
#     class Meta:
#         model = Car
#         fields = ['mark', 'modl', 'color']