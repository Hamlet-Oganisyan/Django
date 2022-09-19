from django.contrib import admin

from .models import Student, Teacher, TeacherStudents

class TeacherStudentsInline(admin.TabularInline):
    model = TeacherStudents


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    inlines = [TeacherStudentsInline,]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
