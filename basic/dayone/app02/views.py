from django.shortcuts import render
from django.http import HttpResponse as res

# Create your views here.
def about(request):
  
  return render(request, 'app2/about.html')