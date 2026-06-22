from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import JsonResponse
def studentsView(request):
  students = {
      "id":1,
      "name":"rajes",
      "age":23
    }
  
  return  JsonResponse(students)