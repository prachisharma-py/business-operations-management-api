from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from operations.models import Operation
from operations.api.serializers import OperationReadSerializer, OperationWriteSerializer

from operations.api.permissions import OperationPermission
from operations.api.filters import OperationFilter


# Create your views here.

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.select_related(
        "department", 
        "assigned_to",
        "assigned_to__user",
    ).all()

    permission_classes = [OperationPermission]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = OperationFilter

    search_fields = [
        "title",
        "description",
    ]

    ordering_fields = [
        "title",
        "created_at",
    ]

    ordering = ("-created_at",)


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return OperationReadSerializer

        return OperationWriteSerializer
