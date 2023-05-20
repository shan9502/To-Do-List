from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import Users
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def UserRegisterView(request):
    print(request.data)
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        print(serializer.validated_data['name'])
        user = Users.objects.create(
            name=serializer.validated_data['name'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        # You can perform additional actions here, such as sending a confirmation email

        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)