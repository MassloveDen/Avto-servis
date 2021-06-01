from django.db import models

# import dilers.car
#  Create your models here.
# from dilers.car.models import Car


class Sail(models.Model):
    sail = models.PositiveIntegerField("Цена продажи", default=0, help_text="Цена")

    def __str__(self):
        return str(self.sail)

    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Стоимость продажи"


class Repair(models.Model):
    repair = models.PositiveIntegerField("Цена ремонта", default=0, help_text="Цена")

    def __str__(self):
        return str(self.repair)

    class Meta:
        verbose_name = "Ремонт"
        verbose_name_plural = "Стоимость ремонта"



class SkladZap(models.Model):
    name = models.CharField("Наименование склада", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Склад запчастей"
        verbose_name_plural = "Склады запчастей"



class Zapas(models.Model):
    name = models.CharField("Название", max_length=20)
    zapas = models.ManyToManyField(SkladZap, verbose_name="Запасные части")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Запчасть"
        verbose_name_plural = "Запчасти"


class SkladAvto(models.Model):
    name = models.CharField("Наименование склада", max_length=30)
    # avto = models.ForeignKey(Car, verbose_name="Запасные части", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Склад авто"
        verbose_name_plural = "Склады авто"



class Uslugi(models.Model):

    title = models.CharField("Название центра", max_length=100)
    # centr_pic = models.ImageField("Изображение центра", upload_to="static/img/")
    sail = models.ForeignKey(Sail, verbose_name="Стоимость продажи", on_delete=models.CASCADE)
    repair = models.ForeignKey(Repair, verbose_name="Стоимость ремонта", on_delete=models.CASCADE)
    sklad_zap = models.ForeignKey(SkladZap, verbose_name="Склад запчастей", on_delete=models.CASCADE)
    sklad_avto = models.ForeignKey(SkladAvto, verbose_name="Склад авто", on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'