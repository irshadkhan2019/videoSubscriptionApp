from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from course.models import Course
# Create your views here.
# Buy course
@login_required(login_url='authentication:login')
def buy_course(request,course_id):
    course = get_object_or_404(Course, pk=course_id)

    context = {
        "course": course,
    }
    return render(request, 'buy_course.html',context)