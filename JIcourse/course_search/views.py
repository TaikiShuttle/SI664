from django.shortcuts import render, get_object_or_404

from course_search.models import Course

# Create your views here.
def greet(request):
    return render(request = request, template_name = 'course_search/greet.html') 

def result(request, course_id:str):
    course = get_object_or_404(Course, course_id = course_id)
    return render(request = request, template_name = "course_search/result.html", context = {'course':course})