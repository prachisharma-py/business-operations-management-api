from django_filters import rest_framework as filters

from operations.models import Operation


class OperationFilter(filters.FilterSet):
    class Meta:
        model = Operation
        fields = (
            "department",
            "status",
            "assigned_to",
        ) 
