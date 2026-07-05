from rest_app.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



# manually way to convert model data into jsno 
    # students = Student.objects.all()
    # students_list = list(students.values())
    # return JsonResponse(students_list , safe=False)

# using serializer file convert queryset into json
@api_view(["GET" , "POST"])
def studentsView(request):

   if request.method == "GET":
      # get all te data from student table
      students = Student.objects.all()
      serializer = StudentSerializer(students , many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)
   
   elif request.method == "POST":
      serializer = StudentSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  #  else:
  #     return Response({"error":"No students are available at this time"}, status=status.HTTP_404_NOT_FOUND)

