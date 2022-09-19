# Generated by Django 4.1.1 on 2022-09-17 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_remove_student_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', through='school.TeacherStudents', to='school.teacher'),
        ),
        migrations.AlterField(
            model_name='teacherstudents',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student'),
        ),
        migrations.AlterField(
            model_name='teacherstudents',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.teacher'),
        ),
    ]
