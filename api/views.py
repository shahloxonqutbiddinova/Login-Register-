from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")

        user = User(username = username)
        user.set_password(password)
        user.save()

        data = {
            "status": True,
            "message": "User registered successfully."
        }

        return Response(data)

class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)

        data = {
            "status": True,
            "message": "User logged successfully",
            "token": {
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }
        }

        return Response(data)
