from django.views import generic
from .models import *

# Create your views here.
from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'Exam_Info/index.html'
    context_object_name = 'ExamList'

    def get_queryset(self):
        return {
            Exam.objects.order_by('-time')[0:2]
        }

class ExamDetailView(generic.DetailView):
    template_name = 'Exam_Info/ExamDetails.html'
    model = Exam
    context_object_name = 'NowExam'

    def get_queryset(self):
        return Exam.objects.order_by('-time')

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