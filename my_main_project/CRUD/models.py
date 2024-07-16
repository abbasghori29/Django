from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no=models.CharField(max_length=20,default=None)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    def __str__(self):
        return self.roll_no


