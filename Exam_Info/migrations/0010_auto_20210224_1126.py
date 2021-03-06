# Generated by Django 2.2.19 on 2021-02-24 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_Info', '0009_auto_20210224_1053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': '班级', 'verbose_name_plural': '班级'},
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': '考试', 'verbose_name_plural': '考试'},
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', '男'), ('F', '女'), ('N', '保密')], help_text='性别', max_length=1, verbose_name='性别'),
        ),
    ]
