from rest_framework import serializers

from .models import Employee
from .utils import get_address


class EmployeeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # setting the address trough the zipcode before saving the instance
        address = get_address(validated_data)
        validated_data = {**validated_data, **address}
        employee = Employee(**validated_data)
        employee.save()
        return employee

    class Meta:
        model = Employee
        fields = '__all__'
