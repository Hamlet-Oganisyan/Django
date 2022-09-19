# Generated by Django 4.1.1 on 2022-09-15 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_alter_student_id_alter_studentteacher_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentteacher',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.student'),
        ),
        migrations.AlterField(
            model_name='studentteacher',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='school.teacher'),
        ),
    ]
