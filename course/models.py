from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_free = models.BooleanField(default=True) 
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)  


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_url = models.URLField(blank=True, null=True)  # URL to the video
    video_file = models.FileField(upload_to='course_videos/', blank=True, null=True)  # Dynamic upload path    