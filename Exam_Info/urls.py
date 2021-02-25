from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('exam/', views.ExamOverView.as_view(), name = 'exam_all'),
    path('exam/exam_details/<str:exam_title>/', views.ExamDetailView.as_view(), name = 'exam_details'),
    # 1. 需要传递的内容包括：
    #    title(用以描述本次考试，记录为字符串，格式为“考试<...>的<...>科目”), Value_min, Value_max, Value_Q1, Value_Q2, Value_Q3,
    #    Value_ScoreMax(用以表示本次考试该科目理论最高分)
    # 2. 同时还有Value_Bar10Score, Value_Bar10
    path('class/', views.ClassOverView.as_view(), name = 'class_all'),
    path('class/<int:pk>/class_details/', views.ClassDetailView.as_view(), name = 'class_details')
#    re_path(r'^students_contrast/$', views.ContrastStudentsView, name = 'students_contrast') # 多学生对比分析路由
]