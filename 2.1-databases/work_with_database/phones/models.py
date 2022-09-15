from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField(max_length=200, verbose_name='image')
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='release_date')
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=150, unique=True)
