from rest_framework import serializers

from accounts.api.serializers import UserSerializer
from employees.models import Employee


class EmployeeReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = (
            "id",
            "employee_id",
            "department",
            "designation",
            "joining_date",
            "employee_status",
            "user",
            "created_at",
            "updated_at",
        )


class EmployeeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "user",
            "employee_id",
            "department",
            "designation",
            "joining_date",
            "employee_status",
        )
