from django.db import models

# Create your models here.
class PintuData(models.Model):
  name=models.CharField(max_length=100)
  roll=models.IntegerField()
  email=models.EmailField(max_length=200)
  city=models.CharField(max_length=150)
 
  
  def __str__(self):
    return self.name
  
class Result(models.Model):
  name=models.CharField(max_length=100)
  roll=models.IntegerField()
  marks=models.IntegerField()
  
  def __str__(self):
    return self.name