from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=10, required=True)
    reset_password = serializers.CharField(max_length=10, required=True)

    def validate_username(self, value):
        if User.objects.filter(username = value).exists():
            raise serializers.ValidationError("User bazada mavjud")

        return value

    def validate(self, data):
        password = data['password']
        password2 = data['reset_password']
        if password != password2:
            raise serializers.ValidationError("Parollar bir xil emas.")

        return data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    passwors = serializers.CharField(required=True)
