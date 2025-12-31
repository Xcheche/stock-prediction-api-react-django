from django.urls import path
from .import views


urlpatterns = [
    path('', views.students, name='students'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
]