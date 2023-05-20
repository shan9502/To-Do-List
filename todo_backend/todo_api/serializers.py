from rest_framework import serializers
from .models import Users
from .models import TodoList

class UserSerializer(serializers.Serializer):
    class Meta:
        model = Users
        fields = '__all__'

class TodoListSerializer(serializers.Serializer):
    class Meta:
        model = TodoList
        fields = '__all__'