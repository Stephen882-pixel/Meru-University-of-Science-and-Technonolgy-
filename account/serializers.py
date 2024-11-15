from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=50)
    lastname = serializers.CharField(max_length=50)
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):

        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already exists")

        return data

    def create(self, validated_data):
        user = User.objects.create(first_name=validated_data['firstname'],
            last_name=validated_data['lastname'],
            username=validated_data['username'].lower()
            )
        user.set_password(validated_data['password'])

        return validated_data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
      if not User.objects.filter(username=data['username']).exists():
          raise serializers.ValidationError("account does not exist")

      return data

    def get_jwt_token(self, data):

        user = authenticate(username = data['username'],password =  data['password'])

        if not user:
            return {'message': 'Invalid Credentials','data':{}}

        refresh = RefreshToken.for_user(user)

        return {
            'message': 'Login successful',
            'data': {
                'token': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }
            }
        }



