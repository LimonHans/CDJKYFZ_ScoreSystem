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
    title = models.CharField(blank = False, max_length = 200, help_text = "考试标题", default = "未指定标题")
    
    description = models.TextField(blank = True, help_text = "考试描述", default = "无描述")

    # 考试时间
    time = models.DateField()

    def __str__(self):
        return self.title

# 学生类
class Student(models.Model):
    # 姓名
    name = models.CharField(null = False, blank = False, max_length = 10, help_text = "学生姓名", default = "无名氏")

    def __str__(self):
        return self.name