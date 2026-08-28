from rest_framework import serializers

from operations.models import Operation


class OperationReadSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    assigned_to = serializers.SerializerMethodField()

    class Meta:
        model = Operation
        fields = (
            "id",
            "title",
            "description",
            "department",
            "assigned_to",
            "status",
            "created_at",
            "updated_at",
        )


    def get_assigned_to(self, obj):
        if obj.assigned_to is None:
            return None

        return {
            "id": obj.assigned_to.id,
            "employee_id": obj.assigned_to.employee_id,
            "name": (
                obj.assigned_to.user.get_full_name() or obj.assigne_to.user.username
            ),
            "designation": obj.assigned_to.designation, 
        }


class OperationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = (
            "title",
            "description",
            "department",
            "assigned_to",
            "status",
        )

    def validate(self, attrs):
        department = attrs.get(
            "department",
            getattr(self.instance, "department", None),
        )

        assigned_to = attrs.get(
            "assigned_to",
            getattr(self.instance, "assigned_to", None),
        )

        if assigned_to is not None and assigned_to.department_id != department.id:
            raise serializers.ValidationError(
                {
                    "assigned_to": (
                        "The assigned employee must belong to the selected department."
                    )
                }
            )

        return attrs
   