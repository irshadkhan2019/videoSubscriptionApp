import matplotlib
matplotlib.use('agg')  # to avoid not in loop 
import matplotlib.pyplot as plt
from django.conf import settings
from .models import Course,UserCourses
from django.db.models import Count
import os

# Function to generate top 5 purcahsed courses as bar plt.
def generate_top_purchased_courses():
    course_purchases = Course.objects.annotate(num_purchases=Count('usercourses'))

    if not course_purchases.exists():
        # If there are no courses with purchases, return None or an appropriate response
        return None
   
    # Sort the courses by the number of purchases in descending order and select the top 5
    top_courses = course_purchases.order_by('-num_purchases')[:5]
    print(top_courses)

    course_names = [course.title for course in top_courses]
    purchase_counts = [course.num_purchases for course in top_courses]

    # Create a bar graph
    plt.bar(course_names, purchase_counts)
    plt.xlabel('Courses')
    plt.ylabel('Number of Purchases')
    plt.title('Top 5 Most Purchased Courses')

    # Define the path to save the image in the media folder
    media_root = settings.MEDIA_ROOT
    image_path = os.path.join(media_root, 'top_courses.png')

    # Save the plot as an image
    plt.tight_layout()
    plt.savefig(image_path)

    # Pass the image file to the template
    image_url = os.path.join(settings.MEDIA_URL, 'top_courses.png')

    return image_url