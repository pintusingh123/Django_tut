from django.urls import path
from formapp2.views import register
urlpatterns = [
    path('register/', register, name='register' )
]
