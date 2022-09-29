from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from course_search.models import Course
from django.views import View

# Create your views here.
def greet(request):
    return render(request = request, template_name = 'course_search/greet.html') 

class Search(View):
    def get(self, request):
        return render(request = request, template_name = "course_search/search.html")

    def post(self, request):
        course_id = request.POST.get('course_id')
        return HttpResponseRedirect(course_id)

class Add(View):
    def get(self, request):
        return render(request = request, template_name = 'course_search/add.html')

    def post(self, request):

        # read in the course information
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course_name')
        instructor = request.POST.get('instructor')
        last_offered = request.POST.get('last_offered')
        credit = float(request.POST.get('credit'))
        category = request.POST.get('category')
        avg_rating = float(request.POST.get('average_rating'))

        # check whether the database already has this record, 1 indicates there is a record, which means insertion should be forbidden, 0 means good
        identical_flag = Course.objects.filter(course_id = course_id, course_name = course_name, instructor = instructor, last_offered = last_offered, credit = credit, category = category,
        avg_rating = avg_rating).count()

        if identical_flag:
            request.session['fail_course_id'] = course_id
            return HttpResponseRedirect('add_fail')

        # create a course instance
        course = Course(course_id = course_id, course_name = course_name, instructor = instructor, last_offered = last_offered, credit = credit, category = category,
        avg_rating = avg_rating)

        # save the course to the database
        course.save()

        # add the course id to the session so that the success site will be able to use it
        request.session['success_course_id'] = course_id

        return HttpResponseRedirect('add_success')

def add_success(request):
    # get the course_id of the successfully added course
    course_id = request.session.get('success_course_id', False)

    # if there is indeed a course added
    if course_id:
        # delete the record from the session
        del(request.session['success_course_id'])

        return render(request = request, template_name = 'course_search/add_success.html', context = {'course_id': course_id})

def add_fail(request):
    # get the course_id of the course that fails to add
    course_id = request.session.get('fail_course_id', False)

    # if there is indeed a course failed to be added
    if course_id:
        # delete the record from the session
        del(request.session['fail_course_id'])

        return render(request = request, template_name = 'course_search/add_fail.html', context = {'course_id': course_id})

def result(request, course_id:str):
    course = Course.objects.get(course_id = course_id)
    return render(request = request, template_name = "course_search/result.html", context = {'course': course})

def course_list(request):
    courses = Course.objects.all()
    return render(request = request, template_name = "course_search/course_list.html", context = {'courses': courses})
