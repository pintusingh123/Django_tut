from django.shortcuts import render
from django.http  import HttpResponse as res
# Create your views here.



def index(request, **kwargs):
  status = kwargs.get('status')
  return  render(request, 'app1/home.html', {'status': status})