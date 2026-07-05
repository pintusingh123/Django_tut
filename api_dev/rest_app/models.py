from django.db import models

# Create your models here.
class Student(models.Model):
  student_id=models.CharField(max_length=10)
  name=models.CharField()
  branch=models.CharField()
   

  def __str__(self):
    return self.name