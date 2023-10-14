from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_free = models.BooleanField(default=True) 
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)  

    # display name at admin panel
    def __str__(self):
        return self.title

# video for a course
class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_url = models.URLField(blank=True, null=True)  # URL to the video
    video_file = models.FileField(upload_to='course_videos/', blank=True, null=True)  # Dynamic upload path    

    # display name at admin panel
    def __str__(self):
        return self.title

# Stores courses bought by users
class UserCourses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    purchased_courses = models.ForeignKey(Course,on_delete=models.SET_NULL, blank=True, null=True)

    # display name at admin panel
    def __str__(self):
        return self.user
