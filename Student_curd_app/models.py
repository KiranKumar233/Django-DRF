from django.db import models

# Create your models here.

class StudentList(models.Model):
    Name=models.CharField(max_length=50)
    mobile = models.IntegerField()
    DOB=models.DateField()
    DOJ= models.DateField()
    Course=models.CharField(max_length=50)

