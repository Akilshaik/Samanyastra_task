from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Customuserserializers,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(APIView):
    def post(self, request):
        serializer = Customuserserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            # Creating the JWT tokens
            refresh = RefreshToken.for_user(user)
            
            # Get user data (excludes password)
            user_data = Customuserserializers(user).data

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                **user_data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    