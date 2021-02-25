from django.views import generic
from .models import *
import numpy as np
from django.db.models import Max, Min, Avg

# Create your views here.
from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'Exam_Info/index.html'
    context_object_name = 'ExamList'

    def get_queryset(self):
        return {
            ExamScore.objects.order_by('-time')[0:2]
        }

class ExamOverView(generic.ListView):
    template_name = 'Exam_Info/ExamAll.html'
    model = ExamScore
    context_object_name = 'ExamList'

    def get_queryset(self):
        return ExamScore.objects.order_by('-time').values('exam_title')

class ExamDetailView(generic.DetailView):
    template_name = 'Exam_Info/ExamDetails.html'
    model = ExamScore
    context_object_name = 'NowExam'

    def get_queryset(self):
        self.exam_title = get_object_or_404(ExamScore, exam_title = self.kwargs['exam_title'])
        return ExamScore.objects.filter(exam_title = self.exam_title).order_by('-time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(self.queryset.aggregate(value_max = Max('total_score'))) # 为上下文加入总分最大值
        context.update(self.queryset.aggregate(value_min = Min('total_score'))) # 为上下文加入总分最小值
        context['value_Q1'], context['value_Q2'], context['value_Q3'] = np.percentile(list(self.queryset.values('total_score')), [25, 50, 75]) # 同理，总分的四分

        # 语文
        context.update(self.queryset.aggregate(value_yw_max = Max('yw'))) # 为上下文加入最大值
        context.update(self.queryset.aggregate(value_yw_min = Min('yw'))) # 为上下文加入最小值

        # 数学
        context.update(self.queryset.aggregate(value_sx_max = Max('sx')))
        context.update(self.queryset.aggregate(value_sx_min = Min('sx')))

        # 英语
        context.update(self.queryset.aggregate(value_yy_max = Max('yy')))
        context.update(self.queryset.aggregate(value_yy_min = Min('yy')))

        # 物理
        context.update(self.queryset.aggregate(value_wl_max = Max('wl')))
        context.update(self.queryset.aggregate(value_wl_min = Min('wl')))

        # 化学
        context.update(self.queryset.aggregate(value_hx_max = Max('hx')))
        context.update(self.queryset.aggregate(value_hx_min = Min('hx')))

        # 生物
        context.update(self.queryset.aggregate(value_sw_max = Max('sw')))
        context.update(self.queryset.aggregate(value_sw_min = Min('sw')))

        subjects = ('yw', 'sx', 'yy', 'wl', 'hx', 'sw')

        for subject in subjects:
            context[f'value_{subject}_Q1'], context[f'value_{subject}_Q2'], context[f'value_{subject}_Q3'] = np.percentile(list(self.queryset.values(subject)), [25, 50, 75]) # 同理，各个学科的四分

class ClassOverView(generic.ListView):
    template_name = 'Exam_Info/ClassAll.html'
    model = Class
    context_object_name = 'ClassList'

    def get_queryset(self):
        return Class.objects.order_by('name')

class ClassDetailView(generic.DetailView):
    template_name ='Exam_Info/ClassDetails.html'
    model = Class
    context_object_name = 'NowClass'

    def get_queryset(self):
        return Class.objects.order_by('-time')

#def ContrastStudentsView(request):
#    # TODO
#    pass