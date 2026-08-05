from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializers import LoginSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(
    summary="Login",
    description="Authenticate a user and return JWT access and refresh tokens.",
    tags=["Authentication"],
)

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
