from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('exams/<int:pk>/exam_details/', views.DetailView.as_view(), name = 'exam_details')
]