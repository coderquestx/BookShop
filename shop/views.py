from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse, Http404
from .models import Category, Course

def index(request):
    courses = Course.objects.all()
    print(courses)
    return render(request, 'shop/courses.html', {'courses':courses})

def single_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/single_course.html', {'course':course})
