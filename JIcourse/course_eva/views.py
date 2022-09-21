from django.shortcuts import render

# Create your views here.

def greet(request):
    return render(request = request, template_name = "course_eva/greet.html")