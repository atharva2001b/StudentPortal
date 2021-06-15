from django.db import models

# Create your models here.
class Students(models.Model):
    rollnumber=models.IntegerField(default=0)
    year=models.CharField(max_length=3,default="")
    department=models.CharField(max_length=15,default="")
    username=models.CharField(max_length=16,default="")
    password=models.CharField(max_length=15,default="")


    def __str__(self):
        r=str(self.rollnumber)
        return  r

class Questionanswers(models.Model):
    Question=models.CharField(max_length=300,default='')
    Answers=models.CharField(max_length=300,default='')
    rollnumber=models.IntegerField(default=0)
    teacher_id=models.IntegerField(default=0)