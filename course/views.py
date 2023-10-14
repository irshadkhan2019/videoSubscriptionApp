from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course

# show course page only to logged in users
@login_required(login_url='authentication:login')
def course_list(request):
    courses = Course.objects.all()
    course_count = courses.count()
    context = {
        "courses": courses,
        "course_count": course_count,
    }
    return render(request, 'course.html', context)
