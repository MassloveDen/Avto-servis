from django.db import models

# Create your models here.


class Color(models.Model):
    name = models.CharField("Цвет", max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

class Mark(models.Model):
    name = models.CharField("Марка", max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"

class Modl(models.Model):
    name = models.CharField("Модель", max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"





class Car(models.Model):
    title = models.CharField("Авто", max_length=100)
    vin = models.CharField("VIN", max_length=20, primary_key=True, unique=True)
    # car_pic = models.ImageField("Изображение авто", upload_to="static/img/")
    mark = models.ForeignKey(Mark, verbose_name="Марка", on_delete=models.CASCADE)
    modl = models.ForeignKey(Modl, verbose_name="Модель", on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name="Цвет", on_delete=models.CASCADE)
    # sail =
    # repair =
    def __str__(self):
        return f'Автомобиль: {self.title}'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
