from django.shortcuts import render
from .models import Post

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {'Exam_List': Post.objects.all()}

    return render(request, 'Exam_Info/index.html', context = context)