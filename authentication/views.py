from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm

# To Register user
def Signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('authentication:login')  # Redirect to login page upon successful registration
    else:
        form = RegistrationForm()
    
    return render(request, 'signup.html', {'form': form})


def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request, "Logged in successfully")
            return redirect('course:course')
        else:
            messages.error(request, "Username or Password is incorrect!!")

    return render (request,'login.html')

def Logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('authentication:login')