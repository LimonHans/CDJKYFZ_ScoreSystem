from django.db import models

# Create your models here.
import datetime
from django.db import models


# class Post(models.Model):
#     title = models.CharField(max_length = 200)
#     content = models.TextField()

#     def __str__(self):
#         return self.title

# 考试类
class Exam(models.Model):
    # 考试标题
    title = models.CharField(verbose_name = "标题", blank = False, max_length = 200, help_text = "考试标题", default = "未指定标题")
    # 考试描述
    description = models.TextField(verbose_name = "描述", blank = True, help_text = "考试描述", default = "暂无描述")
    value_min = models.IntegerField(blank = False, help_text = "Min Scores", default = 0)
    value_Q1 = models.IntegerField(blank = False, help_text = "Q1 Scores", default = 0)
    value_Q2 = models.IntegerField(blank = False, help_text = "Q2 Scores", default = 75)
    value_Q3 = models.IntegerField(blank = False, help_text = "Q3 Scores", default = 150)
    value_max = models.IntegerField(blank = False, help_text = "Max Scores", default = 150)
    # 考试时间
    time = models.DateField()

    # 年级元组
    GRADES = (
        (1, '高一'),
        (2, '高二'),
        (3, '高三')
    )
    # 考试年级
    grade = models.IntegerField(verbose_name = "考试年级", blank = False, help_text = "选择年级", choices = GRADES, default = 1)
    
    # 参加考试的学生
    students = models.ManyToManyField('Student', default = "")

    def __str__(self):
        return self.title

# This class shouldn't appear in another app. :D
# 学生类
class Student(models.Model):
    # 姓名
    name = models.CharField(verbose_name = "姓名", blank = False, max_length = 10, help_text = "学生姓名", default = "无名氏")
    # 性别元组
    GENDERS = (
        ('M', '男'),
        ('F', '女'),
        ('N', '保密')
    )
    # 性别
    gender = models.CharField(verbose_name = "性别", blank = False, max_length = 1, help_text = "性别", choices = GENDERS)

    def __str__(self):
        return self.name