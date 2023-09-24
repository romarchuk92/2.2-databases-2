from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    ordering = 'group'
    template = 'school/students_list.html'
    object_list = Student.objects.all().order_by(ordering)
    context = {'object_list': object_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = 'group'

    return render(request, template, context)


# def teachers_list(request):
#     # ordering = 'group'
#     template = 'school/students_list.html'
#     object_list = Teacher.objects.all()
#     context = {'object_list2': object_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = 'group'

    return render(request, template, context)