from django.urls import path
from core import views as v1

urlpatterns = [
  path('', v1.home, name='home')
]