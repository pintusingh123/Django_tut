
from django.shortcuts import render , redirect
from formapp.forms import StudentForm
from django.http import HttpResponseRedirect


# # Create your views here.
# form simple use
# def register(request):
#     form = StudentForm()
#     data ={}
#     if request.method == 'POST':
#         f_name = request.POST.get("f_name")
#         l_name = request.POST.get("l_name")
#         email = request.POST.get("email")
#         city = request.POST.get("city")
#         data={
#             'f_name':f_name,
#             'l_name':l_name,
#             'email':email,
#             'city':city
#          }
#         print(data)
#     return render(request, 'stdform/register.html', {'form': form})

# production ready form handling
def register(request):
  std_data= {}
  if request.method == "POST":
    form = StudentForm(request.POST)
    if form.is_valid():
      fname = form.cleaned_data['f_name']
      lname = form.cleaned_data['l_name']
      email = form.cleaned_data['email']
      city = form.cleaned_data['city']
      std_data ={
        'fname':fname,
        'lname':lname,
        'email':email,
        'city':city
      }
      print(std_data)
      return HttpResponseRedirect('/student/success/')
  else:
   form = StudentForm()
  
  
  return render(request, 'stdform/register.html', {'form': form}) 


def success(request):
  return render(request, "stdform/success.html")