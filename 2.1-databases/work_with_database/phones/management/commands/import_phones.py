import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            phones_ = Phone(
                name=phones_['name'],
                image=phones_['image'],
                price=phones_['price'],
                releas_date=phones_['releas_date'],
                lte_exists=phones_['lte_exists'],
                slug=slugify(phones_['name'])
            )
            phones_.save()
