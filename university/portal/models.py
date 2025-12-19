from django.db import models

class Student(models.Model):
    reg_no=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=50)
    father_Name=models.CharField(max_length=50)
    branch=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.reg_no   


class Marks(models.Model):
    subject=models.CharField(max_length=50)
    marks=models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.PROTECT)

