from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from course.models import Course,UserCourses
from .models import Payment
from config import settings

import time  
import razorpay

# authenticate with the razorpay client
client = razorpay.Client(auth=(settings.RZP_KEY_ID, settings.RZP_KEY_SECRET))

# Create the receipt ID by appending the formatted timestamp
timestamp = int(time.time())
formatted_timestamp = time.strftime("%Y%m%d%H%M%S", time.gmtime(timestamp))
receipt_id = f"receipt_id#{formatted_timestamp}"

# Buy course
@login_required(login_url='authentication:login')
def buy_course(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    if UserCourses.objects.filter(user=request.user,purchased_courses=course).exists():
        return redirect('course:course')
    else:    
        # create order for razorpay
        DATA = {
                "amount": float(course.price)*100,  #Its in paise 
                "currency": "INR",
                "receipt": receipt_id,
                "notes": {
                    "key1": "value3",
                    "key2": "value2"
                }
            }
        razorpay_order= client.order.create(data=DATA)
        print(razorpay_order)
        razorpay_order_id= razorpay_order['id']  

        context = {
            "course": course,
            "razorpay_order_id":razorpay_order_id,
            "RZP_KEY_ID":settings.RZP_KEY_ID,
            "razorpay_amount":float(course.price)*100,
        }
        return render(request, 'buy_course.html',context)

# After successfull payment store payment info and course bought in db
@login_required(login_url='authentication:login')
def course_payments(request,course_id):
    # Check if the request is ajax or not
    course = get_object_or_404(Course, pk=course_id)
    if (
        request.headers.get("x-requested-with") == "XMLHttpRequest"
        and request.method == "POST"
    ):
        # Store payment details in payment model
        transaction_id = request.POST.get("transaction_id")
        payment_method = request.POST.get("payment_method")
        status = request.POST.get("status")
        amount = request.POST.get("amount")
        payment = Payment(
            user=request.user,
            transaction_id=transaction_id,
            payment_method=payment_method,
            amount=amount,
            status=status,
            course=course,
        )
        payment.save()

        # create user course
        coursebought=UserCourses(
            user=request.user,
            purchased_courses=course,
        )
        coursebought.save()

        response = {
            "transaction_id": payment.transaction_id,
            "status": payment.status,
        }

        return JsonResponse(response)

# show success page after successfull purchase of course
@login_required(login_url='authentication:login')
def success(request,course_id): 
    course = get_object_or_404(Course, pk=course_id)
    
    context = {
        "course": course,
     }

    return render(request, 'success.html',context)
