from .serializers import UserSerializer, TodoListSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .models import Users, TodoList
from rest_framework.views import APIView
from django.core import serializers
import json

# user registration.
@api_view(['POST'])
def UserRegisterView(request):
    #print(request.data)
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        print(serializer.validated_data['name'])
        user = Users.objects.create(
            name=serializer.validated_data['name'],
            email=serializer.validated_data['email'],
            password= make_password(serializer.validated_data['password'])
        )
        # You can perform additional actions here, such as sending a confirmation email

        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# user login.
@api_view(['POST'])
def UserLoginView(request):
    email = request.data['email']
    password = request.data['password']

    user = Users.objects.filter(email = email).first()

    if user:
        if check_password(password, user.password):
            request.session['UserLogin']= True
            request.session['UserId'] = user.id
            return Response(
                {'message': 'User login successfull'}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'error': 'Incorrect password'}, status=status.HTTP_401_UNAUTHORIZED
            )
    return Response(
                {'error': 'email not registered'}, status=status.HTTP_401_UNAUTHORIZED
            )

# user logout
@api_view(['GET'])
def UserLogoutView(request):
    if 'UserLogin' in request.session:
        request.session.clear()
        return Response(
            {'message': 'User logout'}, status=status.HTTP_200_OK
        )
    else:
        return Response(
            {'error': 'No user found to logout'}, status=status.HTTP_401_UNAUTHORIZED
        )

# add todo
@api_view(['POST'])
def AddToDoView(request):
    # serializer = TodoListSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    if 'UserLogin' in request.session and request.session['UserLogin'] == True:
         user_id = request.session['UserId']
         task = request.data['task']
         description = request.data['description']
         priority = request.data['priority']
         date = request.data['date']
         time = request.data['time']

         TodoList.objects.create(user_id=user_id, task=task, description=description, priority=priority, date=date, time=time)
         return Response( {'message': 'Todo Created'}, status=status.HTTP_201_CREATED)
    else:
        return Response( {'message': 'Please Login'}, status=status.HTTP_401_UNAUTHORIZED)

# update todo
class UpdateToDoView(APIView):

    def get(self,request,pk):
        if 'UserLogin' in request.session and request.session['UserLogin'] == True:
            data = serializers.serialize('json', TodoList.objects.filter(id = pk))
            # parsed_data = json.loads(data)
            # for item in parsed_data:
            #     fields = item['fields']
            #     user = fields['user']
            #     task = fields['task']
            #     description = fields['description']
            #     priority = fields['priority']
            #     date = fields['date']
            #     time = fields['time']
            #     status = fields['status']
            #     created_at = fields['created_at']
        return Response( {data})

