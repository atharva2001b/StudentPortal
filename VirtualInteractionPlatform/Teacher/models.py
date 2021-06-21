from django.db import models


# Create your models here.
class Teacher(models.Model):
    Teacher_userid=models.CharField(max_length=20,default='')
    Teacher_password=models.CharField(max_length=20,default='')
    department=models.CharField(max_length=10,default='')
