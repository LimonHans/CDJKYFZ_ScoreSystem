# Generated by Django 2.2.19 on 2021-03-07 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_Info', '0013_auto_20210225_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={},
        ),
        migrations.RemoveField(
            model_name='exam',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='students',
        ),
        migrations.AddField(
            model_name='examscore',
            name='description',
            field=models.TextField(blank=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='description',
            field=models.TextField(blank=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='title',
            field=models.CharField(default='未知考试', max_length=200, verbose_name='考试标题'),
        ),
        migrations.AlterField(
            model_name='examscore',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam_Info.Exam'),
        ),
    ]
