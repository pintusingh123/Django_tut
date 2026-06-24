from django.urls import path
from . import views
urlpatterns = [
  #  cookies operations

  path("set-cookies/", views.set_cookies,name='set-cookies'),

  path("get-cookies/", views.get_cookies,name='get-cookies'),

  path("delete-cookies/", views.delete_cookies,name='delete_cookies'),

  # it is for session operations
    # path("set-session/", views.set_session,name="set_session"),

    # path("get-session/", views.get_session,name="get_session"),

    # path("delete-session/", views.delete_session,name="delete_session"),
]
