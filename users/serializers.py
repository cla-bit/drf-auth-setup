from django.contrib.auth import authenticate
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class CustomRegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = PhoneNumberField(required=True, region="NG")
    agreement = serializers.BooleanField(required=True)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get("first_name")
        user.last_name = self.validated_data.get("last_name")
        user.phone_number = self.validated_data.get("phone_number")
        user.agreement = self.validated_data.get("agreement")
        user.save()
        return user


class CustomLoginSerializer(LoginSerializer):
    username = None
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

        user = authenticate(self.context["request"], email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password")
        if not user.is_verified:
            raise serializers.ValidationError("Email not verified")

        # 🔑 Generate tokens manually
        refresh = RefreshToken.for_user(user)
        print(f"Access token={str(refresh.access_token)}")
        print(f"Refresh token={str(refresh)}")
        attrs["user"] = user
        attrs["access"] = str(refresh.access_token)
        attrs["refresh"] = str(refresh)
        return attrs