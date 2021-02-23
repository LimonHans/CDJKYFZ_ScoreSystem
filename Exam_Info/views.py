from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.
from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'Exam_Info/index.html'
    context_object_name = 'Exam_List'

    def get_queryset(self):
        return Exam.objects.order_by('-time')
    
class DetailView(generic.DetailView):
    template_name = 'Exam_Info/ExamDetails.html'
    model = Exam
    context_object_name = 'Exam_List'
