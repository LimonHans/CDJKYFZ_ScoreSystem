# Generated by Django 2.2.19 on 2021-02-23 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_Info', '0007_auto_20210223_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='班级名称')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='remarks',
            field=models.TextField(blank=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='student',
            name='in_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Exam_Info.Class', verbose_name='所在班级'),
        ),
    ]
