from django.shortcuts import render
from django.views import generic
from .models import Course


# Create your views here.
class CourseListView(generic.ListView):
    template_name = 'content/course_list.html'
    queryset = Course.objects.all()


class CourseDetailView(generic.DetailView):
    template_name = 'content/course_detail.html'
    queryset = Course.objects.all()
