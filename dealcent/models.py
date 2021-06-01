from django.db import models

# Create your models here.
# from dilers.uslugi.models import Uslugi


class DealCent(models.Model):
    name = models.CharField("Название центра", max_length=50)
    # uslugi = models.ForeignKey(Uslugi, verbose_name="Услуги центра", on_delete=models.CASCADE)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дилерский центр"
        verbose_name_plural = "Дилерские центры"
