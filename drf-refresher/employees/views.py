from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
# Create your views here.



#=====CBV ONLY LIST VIEW=====#
"""
class EmployeeList(APIView):
  

    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
          # if the data is not valid, return a 400 bad request response with the error details
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    #Employee detail view to get, update or delete an employee


class EmployeeDetail(APIView):
   
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
          # if the data is not valid, return a 400 bad request response with the error details
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





"""
#------------------------------------------------------------------------------------------------#

#=====MIXINS ONLY LIST VIEW=====#
"""
class EmployeeList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    #List all employees, or create a new employee.
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
#---------------------------get method for listing all employees-----------------#
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
#---------------------------post method for creating a new employee-----------------#
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



#=====MIXINS ONLY DETAIL VIEW=====#
class EmployeeDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    #Retrieve, update or delete an employee instance.
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
#---------------------------get method for retrieving an employee-----------------#
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
#---------------------------put method for updating an employee-----------------#
    def put(self, request, *args, **kwargs):    
        return self.update(request, *args, **kwargs)            
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""        
#------------------------------------------------------------------------------------------------------------------------------------------------------------#




#=====Generics ONLY LIST VIEW=====#
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


#====Generics ONLY DETAIL VIEW=====#
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
   
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer    
    lookup_field = 'pk'