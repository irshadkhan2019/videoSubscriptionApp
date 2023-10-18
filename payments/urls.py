from django.urls import path, include
from . import views

app_name = "payments"

urlpatterns = [
    path("buy_course/<int:course_id>", views.buy_course,name='buy_course'),
    path("course_payments/<int:course_id>", views.course_payments,name='course_payments'),
    path("success/<int:course_id>", views.success,name='success'),
]