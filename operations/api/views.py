from rest_framework import viewsets

from operations.models import Operation
from operations.api.serializers import OperationReadSerializer, OperationWriteSerializer

from operations.api.permissions import OperationPermission


# Create your views here.

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.select_related(
        "department", 
        "assigned_to",
        "assigned_to__user",
    ).all()

    permission_classes = [OperationPermission]


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return OperationReadSerializer

        return OperationWriteSerializer
