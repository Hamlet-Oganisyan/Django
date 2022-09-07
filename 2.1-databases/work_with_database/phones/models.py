from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField(max_length=200)
    release_date = models.DateTimeField()
    lte_exists = models.CharField(max_length=50)
    slug = models.SlugField()
