from django.db import models
from django.utils import timezone

from django.db import models
# Create your models here.

# 班级类
class Class(models.Model):
    name = models.IntegerField(help_text = "数字即可", verbose_name = "班级名称")

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name}班'

# 学生类
class Student(models.Model):
    name = models.CharField(verbose_name = "姓名", max_length = 10, help_text = "学生姓名", default = "无名氏")
    # 性别选项元组
    GENDERS = (
        ('M', '男'),
        ('F', '女'),
        ('N', '保密')
    )
    gender = models.CharField(verbose_name = "性别", max_length = 1, help_text = "性别", choices = GENDERS, blank = True)
    enter_date = models.DateField(verbose_name = "入学时间", default = timezone.now)
    remarks = models.TextField(verbose_name = "备注", blank = True)
    in_class = models.ForeignKey(to = Class, verbose_name = "所在班级", on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 考试类
class Exam(models.Model):
    title = models.CharField(verbose_name = "考试标题", max_length = 200, default = "未知考试")
    description = models.TextField(verbose_name = "备注", blank = True)
    time = models.DateField(verbose_name = "考试时间", default = timezone.now)

    class Meta:
        verbose_name = '考试'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

# 考试信息
class ExamScore(models.Model):
    student = models.ForeignKey(to = Student, verbose_name = "姓名", on_delete = models.CASCADE)
    exam = models.ForeignKey(to = Exam, verbose_name = "考试", on_delete = models.CASCADE)
    description = models.TextField(verbose_name = "备注", blank = True)


    yw = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "语文成绩")
    sx = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "数学成绩")
    yy = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "英语成绩")
    wl = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "物理成绩")
    hx = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "化学成绩")
    sw = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "生物成绩")
    total_score = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "总分")

    grade_rank = models.IntegerField()
    class_rank = models.IntegerField()

    class Meta:
        verbose_name = '考试信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.student}的{self.exam}信息-总分{self.total_score}分'