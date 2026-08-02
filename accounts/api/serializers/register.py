from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "confirm_password",
            "first_name",
            "last_name",
            "phone_number",
            "role",
        )
    
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }


    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {
                    "confirm_password": "Password do not match."
                }
            )
        return attrs


    def validate_password(self, value):
        validate_password(value)
        return value
    

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
