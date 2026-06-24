from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# cookies related fun 
def set_cookies(request):
  response = HttpResponse("coocies set ho gya h")
  response.set_cookie("username","PintuJhala" , max_age=60*60*24*7) # valid for 7 days
  return response

def get_cookies(request):
  username=request.COOKIES.get("username","bintu")
  return HttpResponse(f"coocies get kar liya username :{username}")

def delete_cookies(request):
   response = HttpResponse("coocies delete ho gya h")
   response.delete_cookie("username")
   return response




# session storage emplement fun 
# def set_session(request):
#   request.session['username'] = "pintu"
#   request.session["course"] ="django full tut"
#   return HttpResponse("<h1>set_session data set successfully file</h1>")

# def get_session(request):

#   username = request.session.get("username","Guest")
#   course=request.session.get("course","Not Enrolled")

#   return HttpResponse(f"Welcome : {username}, You are Enrolment is : {course}")

# def delete_session(request):
  
  # one way 
  # try:
  #   del request.session['username']
  #   del request.session['course']
  # except KeyError:
  #   pass


  # # # ssecond easy way
  # request.session.flush() #this will delete all session data at a time
  # return HttpResponse("all session data are deleted done")