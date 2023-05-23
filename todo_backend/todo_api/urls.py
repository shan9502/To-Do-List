from django.urls import path
from .views import (UserRegisterView, UserLoginView, UserLogoutView, AddToDoView, UpdateToDoView)

urlpatterns = [
    path('register/', UserRegisterView, name='registration'),
    path('login/', UserLoginView, name='login'),
    path('logout/', UserLogoutView, name='logout'),
    path('addtodo/', AddToDoView, name='addtodo'),
    path('updatetodo/<int:pk>/',UpdateToDoView.as_view(), name='updatetodo'),
]