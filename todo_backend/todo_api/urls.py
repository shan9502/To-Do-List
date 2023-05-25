from django.urls import path,include
from .views import (UserRegisterView, UserLoginView, UserLogoutView, AddToDoView, UpdateToDoView, ToDoCrudView)
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register (r'todo', ToDoCrudView, basename='todo')

urlpatterns = [
    path('register/', UserRegisterView, name='registration'),
    path('login/', UserLoginView, name='login'),
    path('logout/', UserLogoutView, name='logout'),
    path('addtodo/', AddToDoView, name='addtodo'),
    # path('updatetodo/<int:pk>/',ToDoCrudView.as_view(), name='updatetodo'),
    # router.urls
    path('todo/', include(router.urls), name='todo'),
]