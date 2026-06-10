 
from django.shortcuts import render
from formapp.forms import StudentForm


# Create your views here.
def register(request):
  form = StudentForm()
  
  return render(request, 'stdform/register.html', {'form': form})