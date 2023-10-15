from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
# Buy course
@login_required(login_url='authentication:login')
def buy_course(request,course_id):
        return render(request, 'buy_course.html')