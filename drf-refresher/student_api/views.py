from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from student_api.models import Students
from student_api.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

#------------------------- View to handle GET and POST requests for Students ---------
@api_view(["GET", "POST"])
def students(request):
    # -------- GET all students ----------
    if request.method == "GET":
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # -------- POST / Create student ----------
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#-------------------------Detail View to handle GET, PUT, DELETE for a single Student ---------
@api_view(["GET", "PUT", "DELETE"])
def student_detail(request, pk):
    #----- Fetch the student object by primary key -----
    try:
        students =Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # -------- GET a single student by id ----------
    if request.method=="GET":
        serializer = StudentSerializer(students)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    #-----------------------UPDATE a student by id -----------------------
    elif request.method=="PUT":
        # Getting the existing student object and updating it with new data
        serializer = StudentSerializer(students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #----------------------- DELETE a student by id -----------------------
    elif request.method=="DELETE":
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)