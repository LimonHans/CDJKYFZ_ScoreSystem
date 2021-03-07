from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('exam/', views.ExamOverView.as_view(), name = 'exam_all'),
    path('exam/exam_details/<int:pk>/', views.ExamDetailView.as_view(), name = 'exam_details'),
    # TODO
    # 1. 需要传递的内容包括：(注意有前缀：yw.,sx.,yy.,wl.,hx.,sw.)
    #    .name(用以描述本次考试，记录为字符串，格式为“考试<...>的<...>科目”), .value_min, .value_max, .value_Q1, .value_Q2, .value_Q3,
    #    .value_scoremax(用以表示本次考试该科目理论最高分), .value_rankmax(同理，理论最后一名);
    #    但是在 exam_details 下的页面时，将不要前缀，如在 exam 时的 yw.name 相当于在 该页面下的 name
    # 2. 同时还有value_bar10score[], value_bar20rank[]分别用来描述 从理论最高分到理论最低分的每10分分段、从理论第一名到理论最末名的每20人分段
    # 3. 对于总分，同样也需要 1. 中的内容，前缀：zf
    path('class/', views.ClassOverView.as_view(), name = 'class_all'),
    path('class/<int:pk>/class_details/', views.ClassDetailView.as_view(), name = 'class_details')
#    re_path(r'^students_contrast/$', views.ContrastStudentsView, name = 'students_contrast') # 多学生对比分析路由
]