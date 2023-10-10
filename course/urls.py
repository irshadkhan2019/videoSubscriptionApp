from django.urls import path, include
from . import views

app_name = "course"

urlpatterns = [
    path("course/", views.Course,name='course'),
  
]