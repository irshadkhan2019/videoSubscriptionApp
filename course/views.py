from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course,Video

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

# get all videos related to course and pass to template
@login_required(login_url='authentication:login')
def course_detail(request,course_id,video_id=None):
    course = get_object_or_404(Course, pk=course_id)
    videos = Video.objects.filter(course=course)

    if video_id is 0 :
        video = videos[0] if videos else None
    else:
        video = get_object_or_404(Video, pk=video_id)

    context = {
        'course': course,
        'videos': videos,
        'video':video,
    }
    return render(request, 'course_detail.html', context)   
