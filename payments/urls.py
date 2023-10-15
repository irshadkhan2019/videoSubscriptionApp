from django.urls import path, include
from . import views

app_name = "payments"

urlpatterns = [
    path("buy_course/<int:course_id>", views.buy_course,name='buy_course'),
    
]