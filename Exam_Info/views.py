from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {
        'Exam_List': [
            {
                "title": "图雀写作工具推出了新的版本",
                "content": "随随便便就能写出一篇好教程，真的很神奇",
            },
            {
                "title": "图雀社区正式推出快速入门系列教程",
                "content": "一杯茶的功夫，让你快速上手，绝无担忧",
            },
        ]
    }

    return render(request, 'Exam_Info/index.html', context = context)