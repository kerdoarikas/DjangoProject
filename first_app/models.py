from django.db import models
from django.contrib import admin


class Student(models.Model):
    name = models.CharField(max_length=265)
    birth_of_date = models.DateField(null=True, blank=True)
    weight = models.IntegerField()

class StudentAdmin(admin.ModelAdmin):

    list_filter = ['weight']

    def birthday(self, obj):
        if obj.birth_of_date is not None:
            return obj.birth_of_date.strftime('%d.%m.%Y')

    list_display = ['name', 'birthday', 'weight']

class Teacher(models.Model):
    name = models.CharField(max_length=260)
    subject = models.CharField(max_length=260)

class TeacherAdmin(admin.ModelAdmin):
    list_filter = ['subject']
    list_display = ['name', 'subject']
