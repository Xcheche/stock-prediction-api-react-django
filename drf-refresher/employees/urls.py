from django.urls import path
from .import views


urlpatterns = [
    path('', views.EmployeeList.as_view(), name='employee_list'),
    path('single/<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),
]