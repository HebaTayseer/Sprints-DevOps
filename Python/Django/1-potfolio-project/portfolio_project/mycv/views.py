
from django.http import HttpResponse
from django.template import loader
from .models import Students, Courses
from django.views.generic.list import ListView
from django.shortcuts import HttpResponse, render, redirect
from .forms import InputForm, StudentForm, PostForm


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


# Create your views here.
'''
def home_views(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "home.html", context)
'''


def home_view(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
    # save the form data to model
    context = {}
    context['StudentForm'] = StudentForm()
    return render(request, "home.html", context)






def home(request):
    # check if the request is post
    if request.method == 'POST':

        # Pass the form data to the form class
        details = PostForm(request.POST)

        # In the 'form' class the clean function
        # is defined, if all the data is correct
        # as per the clean function, it returns true
        if details.is_valid():

            # Temporarily make an object to be add some
            # logic into the data if there is such a need
            # before writing to the database
            post = details.save(commit=False)

            # Finally write the changes into database
            post.save()

            # redirect it to some another page indicating data
            # was inserted successfully
            return HttpResponse("data submitted successfully")

        else:

            # Redirect back to the same page if the data
            # was invalid
            return render(request, "home1.html", {'form': details})
    else:

        # If the request is a GET request then,
        # create an empty form object and
        # render it into the page
        form = PostForm(None)
        return render(request, 'home1.html', {'form': form})

