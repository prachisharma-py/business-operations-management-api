from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import UserSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(
    summary="Get current user",
    description="Retrieve the profile of the currently authenticated user.",
    responses=UserSerializer,
    tags=["Authentication"],
)
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
