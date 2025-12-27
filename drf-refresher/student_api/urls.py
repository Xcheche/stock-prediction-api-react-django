from django.urls import path
from .import views


urlpatterns = [
    path('', views.get_students, name='get_students'),
    path('json/', views.get_students_json, name='get_students_json'),
]