# Generated by Django 4.1.1 on 2022-09-15 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_teacherposition'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeacherPosition',
            new_name='StudentTeacher',
        ),
    ]
