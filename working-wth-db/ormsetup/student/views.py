from student.models import Profile
from django.shortcuts import render

# Create your views here.
def show(request):
  all_data = Profile.objects.all()
  return render(request, 'student/show.html', {'data': all_data})