# Generated by Django 4.1.7 on 2023-05-17 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='user_id',
            new_name='user',
        ),
    ]