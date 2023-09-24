from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
    # list_display = ['id', 'name', 'teachers', 'group']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
    # list_display = ['id', 'name', 'subject']
