from django.db import models


# Create your models here.
class Teacher(models.Model):
    Teacher_userid=models.CharField(max_length=20)
    Teacher_password=models.CharField(max_length=20)