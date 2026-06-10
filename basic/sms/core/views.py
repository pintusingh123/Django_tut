from django.shortcuts import render

# def home(request):
#     return render(request, "core/home.html")
from django.http import HttpResponse


def base(request):
    return render(request, "core/base.html")
    # return HttpResponse("Hello, this is the base view.")

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")