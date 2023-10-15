from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from course.models import Course
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
   # create order for razorpay
    DATA = {
            "amount": int(course.price),
            "currency": "INR",
            "receipt": receipt_id,
            "notes": {
                "key1": "value3",
                "key2": "value2"
            }
        }
    razorpay_order=client.order.create(data=DATA)
    print(razorpay_order)   

    context = {
        "course": course,
     }
    return render(request, 'buy_course.html',context)