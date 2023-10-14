from django.contrib import admin
from .models import Course,Video,UserCourses
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display=("title","description","price","is_free")
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class VideoAdmin(admin.ModelAdmin):
    list_display=("course","title","video_url","video_file")
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
  
class UserCoursesAdmin(admin.ModelAdmin):
    list_display=("user","purchased_courses")
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# showing interface to admin users
admin.site.register(Course, CourseAdmin)    
admin.site.register(Video, VideoAdmin)
admin.site.register(UserCourses, UserCoursesAdmin)

