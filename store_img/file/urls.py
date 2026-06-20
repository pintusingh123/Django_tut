from django.urls import path
from .views import upload_file ,profile_view

urlpatterns = [
    path('form/', upload_file  , name="upload_file" ),

     path('profile/', profile_view  , name="profile_view" )
]
