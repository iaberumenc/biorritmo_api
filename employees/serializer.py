from rest_framework import serializers, validators
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','curp','fecha_nacimiento')
        extra_kwargs = {'curp': {
                    'validators': [
                        validators.UniqueValidator(
                            queryset=Employee.objects.all(),message='Ya existe un empleado registrado con ese curp'
                        )
                    ]}}