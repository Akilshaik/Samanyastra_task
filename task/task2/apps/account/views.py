from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import CustomUserSerializers,DashboardSerializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate



class RegisterView(APIView):
    def post(self, request):
        serializer = CustomUserSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({"detial":"Registration successfull",
                "user": CustomUserSerializers(user).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "detail":"Login successful",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class Dashboard(APIView):
    
    permission_classes=[IsAuthenticated]
    def get(self, request):
        serializer = DashboardSerializers(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)



# Create your views here.
