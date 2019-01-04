from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.exceptions import APIException

from .models import Employee
from .serializers import EmployeeSerializer
from .utils import get_address


@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'Employee List': reverse(
                'employee-list', request=request, format=format
            )
        }
    )


class EmployeeListCreate(generics.ListCreateAPIView):
    '''
    Endpoint to list all the users and create a user
    '''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Endpoint to detail the information of a single Employee
    Methods allowed: GET, PUT, DELETE
    '''

    def get(self, request, pk):
        # getting one employee object using the primary key
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, validated_data, pk):
        # setting the data to be easier to manipulate
        data = validated_data.data

        # getting one employee object using the primary key
        employee = get_object_or_404(Employee, pk=pk)

        # verifying if the zipcode changed avoiding another request
        if employee.cep != data['cep']:
            address = get_address(data)
            data = {**data, **address}

        # serializing the employee data
        serializer = EmployeeSerializer(employee, data=data)

        # validating the information in the serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # getting one employee object using the primary key
        employee = get_object_or_404(Employee, pk=pk)
        employee_name = employee.name
        # trying to delete the employee model object
        try:
            employee.delete()
            return Response(
                {
                    'message': 'User {} was deleted.'.format(employee_name)
                },
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            raise APIException({'error': e})
