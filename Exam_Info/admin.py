from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# Plugin: Import Export
class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        export_order = ('id', 'name', 'gender')

# Admin for models
@admin.register(Exam)
class ExamAdmin(ImportExportModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    pass

@admin.register(Class)
class ClassAdmin(ImportExportModelAdmin):
    pass