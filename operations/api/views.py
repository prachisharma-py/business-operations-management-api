from rest_framework import viewsets

from operations.models import Operation
from operations.api.serializers import OperationReadSerializer, OperationWriteSerializer

# Create your views here.

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.select_related(
        "department", 
        "assigned_to",
        "assigned_to__user",
    ).all()


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return OperationReadSerializer

        return OperationWriteSerializer
