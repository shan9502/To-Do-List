from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = 'users'

class TodoList(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True)
    priority = models.CharField(choices=[(1,'Low'), (2,'Normal'), (3,'High')], default='Normal', max_length=20)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now=True)
    status = models.BooleanField(default=0)
    class Meta:
        db_table = 'todo_list'