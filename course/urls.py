from django.urls import path, include
from . import views

app_name = "course"

urlpatterns = [
    path("", views.course_list,name='course'),
    path("course/", views.course_list,name='course'),
    path("course/<int:course_id>/video/<int:video_id>/", views.course_detail,name='course_detail'),
    path("course/purchased", views.purchased_course,name='purchased_course'),
    path("course/top_purchased_courses", views.top_purchased_courses,name='top_purchased_courses'),
  
]