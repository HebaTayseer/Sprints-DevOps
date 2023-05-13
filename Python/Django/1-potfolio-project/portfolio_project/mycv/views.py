from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Students, Courses
from django.views.generic.list import ListView


# Create your views here.
def Welcome(request):
    template = loader.get_template('mycv.html')
    return HttpResponse(template.render())


def list_view(request):
    # dictionary for initial data with field names as keys
    context = {}
    # add the dictionary during initialization
    context["dataset"] = Students.objects.all()
    return render(request, "list_view.html", context)


class CoursesList(ListView):
    # specify the model for list view
    model = Courses
