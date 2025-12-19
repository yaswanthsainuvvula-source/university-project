from django.contrib import admin
from .models import Student, Marks

class StudentAdmin(admin.ModelAdmin):
    list_display=['reg_no','name','father_Name','branch']

class MarksAdmin(admin.ModelAdmin):
    list_display=['subject','marks','student']

admin.site.register(Student,StudentAdmin)
admin.site.register(Marks,MarksAdmin)
