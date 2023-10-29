from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Course,Video,UserCourses
from django.core.paginator import Paginator
from .utils import generate_top_purchased_courses


# show course page only to logged in users
@login_required(login_url='authentication:login')
def course_list(request):
    courses = Course.objects.all()
    course_count = courses.count()

    # Number of items to display per page
    items_per_page = 3
    paginator = Paginator(courses, items_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        "courses": page,
        "course_count": course_count,
    }
    return render(request, 'course.html', context)

# get all videos related to course and pass to template
@login_required(login_url='authentication:login')
def course_detail(request,course_id,video_id=None):
    course = get_object_or_404(Course, pk=course_id)
    videos = Video.objects.filter(course=course)

    # Check if the course is free or the user has purchased it
    if course.is_free or UserCourses.objects.filter(user=request.user,purchased_courses=course).exists():
        if video_id == 0 :
            video = videos[0] if videos else None
        else:
            video = get_object_or_404(Video, pk=video_id)

        context = {
            'course': course,
            'videos': videos,
            'video':video,
        }
        return render(request, 'course_detail.html', context) 
    else:
        # If the course is paid and the user hasn't purchased it, let payments app handle it
        return redirect('payments:buy_course', course_id=course_id)

# Show users their purchased courses
@login_required(login_url='authentication:login')
def purchased_course(request):
    purchased_courses=UserCourses.objects.filter(user=request.user)
    course_count = purchased_courses.count()
    context={
        'purchased_courses':purchased_courses,
        'course_count':course_count,
    }
    return render(request, 'purchased_course.html',context) 

# view to display top 5 purchased courses
def top_purchased_courses(request):
    image_url = generate_top_purchased_courses()
    return render(request, 'top_courses.html', {'image_url': image_url})