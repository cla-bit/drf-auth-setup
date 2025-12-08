from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from dj_rest_auth.registration.serializers import RegisterSerializer



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