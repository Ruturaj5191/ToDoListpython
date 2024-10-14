from django.db import models

# Create your models here.
class ToDolist(models.Model):
    new_task=models.CharField(max_length=200)
    new_date=models.DateField(max_length=30)