from django.shortcuts import render ,redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages
# Create your views here.


def upload_file(request):
  if request.method == "POST":
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      messages.success(request, "Profile picture uploaded successfully")
      return redirect( "profile_view")
    else:
      messages.error(request, "Error Uploading Profile img")
    
  else:
      form = ProfileForm()
  return render(request, "form.html",{"form":form})




def profile_view(request):
   profile = Profile.objects.all()

   return render(request, "profile_view.html" , {"profiles":profile})

