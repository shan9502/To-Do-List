from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = 'users'

class TodoList(models.Model):
    CHOICES = [
                ('Normal','Normal'),
                ('High','High'),
                ('Medium','Medium'),
                ('Login','Login')
            ]
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True)
    priority = models.CharField(max_length=20, choices=CHOICES,default=0)
    date = models.DateField()
    time = models.TimeField()
    status = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'todo_list'