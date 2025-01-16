from rest_framework import serializers
from apps.jwt_auth.models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class Customuserserializers(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model=CustomUser
        fields=['username', 'email', 'password','confirm_password']
    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        print(f"Attempting to authenticate with username: {username} and password: {password}")
        user = authenticate(username=username, password=password)


        if not user:
            raise AuthenticationFailed("Invalid username or password.")
    
    
        attrs['user'] = user
        return attrs