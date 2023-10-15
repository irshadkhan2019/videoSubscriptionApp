from django.db import models
from django.contrib.auth.models import User
from course.models import Course

# Create your models here.
class Payment(models.Model):
    PAYMENT_METHOD = (
        ("RazorPay", "RazorPay"),  
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=100)
    amount = models.CharField(max_length=10)
    status = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.SET_NULL,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_id