from django.urls import path
from formapp import views
urlpatterns = [
    path('register/', views.register, name='register' )
]
