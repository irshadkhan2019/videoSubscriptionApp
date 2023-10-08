from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# @login_required(login_url='login')
# def HomePage(request):
#     return render (request,'home.html')

def Signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            # return HttpResponse("Your password and conform password are not Same!!")
             messages.warning(request, "password and conform password must be same")  
        if username=="" or email=="" or pass1=="":
            messages.warning(request, "Please fill all fields")  
        if User.objects.filter(username=username).exists():
                messages.error(request, 'A user with this username already exists.')
        elif User.objects.filter(email=email).exists():
                messages.error(request, 'A user with this email address already exists.')

        else:

            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            messages.success(request, "Your account has been registered successfully")
            return redirect('authentication:login')
        
    return render (request,'signup.html')

def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request, "Logged in successfully")
            return redirect('home')
        else:
            # return HttpResponse ("Username or Password is incorrect!!!")
            messages.error(request, "Username or Password is incorrect!!")

    return render (request,'login.html')

def Logout(request):
    logout(request)
    return redirect('authentication:login')