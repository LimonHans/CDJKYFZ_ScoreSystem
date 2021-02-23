from django.db import models
from django.utils import timezone

from django.db import models
# Create your models here.

# 班级类
class Class(models.Model):
    name = models.CharField(verbose_name = "班级名称", max_length = 100)

    def __str__(self):
        return self.name

# 考试类
class Exam(models.Model):
    title = models.CharField(verbose_name = "标题", blank = False, max_length = 200, help_text = "考试标题", default = "未指定标题")
    description = models.TextField(verbose_name = "描述", blank = True, help_text = "考试描述", default = "暂无描述")

    value_min = models.IntegerField(blank = False, help_text = "Min Scores", default = 0)
    value_Q1 = models.IntegerField(blank = False, help_text = "Q1 Scores", default = 0)
    value_Q2 = models.IntegerField(blank = False, help_text = "Q2 Scores", default = 75)
    value_Q3 = models.IntegerField(blank = False, help_text = "Q3 Scores", default = 150)
    value_max = models.IntegerField(blank = False, help_text = "Max Scores", default = 150)

    time = models.DateField(verbose_name = "考试时间", default = timezone.now)

    # 年级选择元组
    GRADES = (
        (1, '高一'),
        (2, '高二'),
        (3, '高三')
    )
    grade = models.IntegerField(verbose_name = "考试年级", blank = False, help_text = "选择年级", choices = GRADES, default = 1)

    # 参加考试的学生
    students = models.ManyToManyField('Student', default = "")

    def __str__(self):
        return self.title

# This class shouldn't appear in another app. :D
# 学生类
class Student(models.Model):
    name = models.CharField(verbose_name = "姓名", max_length = 10, help_text = "学生姓名", default = "无名氏")
    # 性别选项元组
    GENDERS = (
        ('M', '男'),
        ('F', '女'),
        ('N', '保密')
    )
    gender = models.CharField(verbose_name = "性别", max_length = 1, help_text = "性别", choices = GENDERS)
    enter_date = models.DateField(verbose_name = "入学时间", default = timezone.now)
    ######################################
    # 这个肯定要改吧，啥时候注册啥时候入学吗... #
    ######################################
    remarks = models.TextField(verbose_name = "备注", blank = True)
    in_class = models.ForeignKey(to = Class, verbose_name = "所在班级", on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.name

