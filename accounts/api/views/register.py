from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import RegisterSerializer, UserSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(
    summary="Register a new user",
    description="Create a new user account.",
    request=RegisterSerializer,
    responses={
        201: UserSerializer
    },
    tags=["Authentication"],
)
class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "message": "User registered successfully.",
                "user":{
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                },
            },
            status=status.HTTP_201_CREATED,
        )
