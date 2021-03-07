from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
# Register your models here.

# Plugin: Import Export
class StudentResource(resources.ModelResource):
    name = Field(attribute = 'name', column_name = '姓名')
    pk = Field(attribute = 'id', column_name = '考号')
    gender = Field(attribute = 'gender', column_name = '性别')
    in_class = Field(attribute = 'in_class', column_name = '班级', widget = ForeignKeyWidget(Class))

    class Meta:
        model = Student
        export_order = ('id', 'name', 'gender')

class ExamScoreResource(resources.ModelResource):
    grade_rank = Field(attribute = 'grade_rank', column_name = '年级排名')
    class_rank = Field(attribute = 'class_rank', column_name = '班级排名')
    
    yw = Field(attribute = 'yw', column_name = '语文')
    sx = Field(attribute = 'sx', column_name = '数学')
    yy = Field(attribute = 'yy', column_name = '英语')
    wl = Field(attribute = 'wl', column_name = '物理')
    hx = Field(attribute = 'hx', column_name = '化学')
    sw = Field(attribute = 'sw', column_name = '生物')
    total_score = Field(attribute = 'total_score', column_name = '总分')

    student = Field(attribute = 'student', column_name = '考号', widget = ForeignKeyWidget(Student))
    # exam = Field(attribute = 'exam', column_name = '考试标题', default = )
    class Meta:
        model = ExamScore
        fields = ('id', 'student', 'class_rank', 'total_score', 'yw', 'sx', 'yy', 'wl', 'hx', 'sw')

# Admin for models

@admin.register(Class)
class ClassAdmin(ImportExportModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource

@admin.register(Exam)
class ExamAdmin(ImportExportModelAdmin):
    pass

@admin.register(ExamScore)
class ExamScoreAdmin(ImportExportModelAdmin):
    resource_class = ExamScoreResource
