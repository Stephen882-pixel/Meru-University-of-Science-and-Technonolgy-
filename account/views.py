from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import status

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message':'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({
                'data': {},
                'message':'your account has been created'
            },status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                'data': {},
                'message':'That username has already been taken'
            },status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)

            #user = serializer.validated_data['user']
            response = serializer.get_jwt_token(serializer.data)

            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': 'Something went wrong'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


