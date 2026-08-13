from rest_framework import serializers
from departments.models import Department
from employees.models import Employee


class ManagerSummarySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ["id", "name", "designation"]

    def get_name(self, obj):
        return obj.user.get_full_name() or obj.user.username


class DepartmentReadSerializer(serializers.ModelSerializer):
    manager = ManagerSummarySerializer(read_only=True)

    class Meta:
        model = Department
        fields = [
            "id",
            "name",
            "description",
            "manager",
            "created_at",
            "updated_at",
        ]


class DepartmentWriteSerializer(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Department
        fields = [
            "name",
            "description",
            "manager",
        ]

    def validate_manager(self, value):
        if value.employee_status != Employee.ACTIVE:
            raise serializers.ValidationError(
                "Only active employees can be assigned as department managers."
            )
        
        return value
