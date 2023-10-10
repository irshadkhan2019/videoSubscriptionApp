from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
@login_required(login_url='authentication:login')
def Course(request):
    return render (request,'course.html')
