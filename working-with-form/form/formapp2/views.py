from django.shortcuts import render
from formapp2.forms import StudentData
from django.http import HttpResponseRedirect
from .forms import StudentData
from .models import Formdata
# Create your views here.


def register(request):
    data = {}
    form = StudentData()
    if request.method == "POST":
        form = StudentData(request.POST)
        if form.is_valid():
            Username = form.cleaned_data['name']
            Useremail = form.cleaned_data['email']
            city = form.cleaned_data['city']
            # Formdata(name=Username,email=Useremail, city=city)
            Formdata.objects.create(
                username=Username,
                useremail=Useremail,
                city=city
            )

            data = {
                'name': Username,
                'email': Useremail,
                'city': city
            }
            print(data)
            return HttpResponseRedirect('/std/register')

    else:
        form = StudentData()

    return render(request, 'student/register.html', {'form': form})
