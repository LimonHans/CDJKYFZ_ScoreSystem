from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('exam/<int:pk>/exam_details/', views.ExamDetailView.as_view(), name = 'exam_details'),
    path('class/all/', views.ClassOverView.as_view(), name = 'class_all'),
    path('class/<int:pk>/class_details/', views.ClassDetailView.as_view(), name = 'class_details')
#    re_path(r'^students_contrast/$', views.ContrastStudentsView, name = 'students_contrast') # 多学生对比分析路由
]