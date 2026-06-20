from django.urls import path
from .views import pag_view

urlpatterns = [
    path('', pag_view, name="page_view")
]
