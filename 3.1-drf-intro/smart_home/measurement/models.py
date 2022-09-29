from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=10, verbose_name='Наименование датчика')
    description = models.CharField(max_length=50, verbose_name='Описание')

    class Meta:
        ordering = ['id']


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')