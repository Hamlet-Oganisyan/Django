# Generated by Django 4.1.1 on 2022-09-29 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Температура'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='sensor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.FloatField(verbose_name='Температура'),
        ),
    ]