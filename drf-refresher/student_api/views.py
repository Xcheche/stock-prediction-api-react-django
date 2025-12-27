from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

student_data = [
    {'id': 1, 'name': 'Alice', 'age': 20, 'major': 'Computer Science'},
    {'id': 2, 'name': 'Bob', 'age': 22, 'major': 'Mathematics'},
    {'id': 3, 'name': 'Charlie', 'age': 21, 'major': 'Physics'},
]

#-------------Using HttpResponse-----------------   
def get_students(request):
    return HttpResponse(student_data)

#-------------Using JsonResponse-----------------
def get_students_json(request):
    return JsonResponse(student_data, safe=False)