from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.response import Response
from .models import Doctors
from .serializers import DoctorsSerializer

# Create your views here.



#View set
"""
class DoctorsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Doctors.objects.all()
        serializer = DoctorsSerializer(queryset, many=True)
        return Response(serializer.data)

    #Create
    def create(self, request):
        serializer = DoctorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)




    #Retrieve single doctor by id
    def retrieve(self, request, pk=None):
        try:
            doctor = Doctors.objects.get(pk=pk)
        except Doctors.DoesNotExist:
            return Response(status=404)
        serializer = DoctorsSerializer(doctor)
        return Response(serializer.data)


    #Update
    def update(self, request, pk=None):
        try:
            doctor = Doctors.objects.get(pk=pk)
        except Doctors.DoesNotExist:
            return Response(status=404)
        serializer = DoctorsSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    #Delete
    def destroy(self, request, pk=None):
        try:
            doctor = Doctors.objects.get(pk=pk)
        except Doctors.DoesNotExist:
            return Response(status=404)
        doctor.delete()
        return Response(status=204)
"""

#---------------------------------Model view set-----------------------------
class DoctorsViewSet(viewsets.ModelViewSet):
    ##Model view set automatically provides implementations for list, create, retrieve, update, and destroy actions.
    #Can filter, search, and order results using built-in features.
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer