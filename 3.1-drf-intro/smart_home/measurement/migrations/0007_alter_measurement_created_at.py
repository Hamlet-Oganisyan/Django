# Generated by Django 4.1.1 on 2022-09-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0006_alter_sensor_description_alter_sensor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]
