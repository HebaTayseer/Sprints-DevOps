Make project called portofolio and show your cv in html page using Django . /n

1) Installing python /n
2) Install a package manager like PIP /n
3) Create virtual environment : python3 -m venv env_name /n
4) Activate the environment : source env_name/bin/activate /n
5) Install Django : python -m pip install Django /n
   Check the dkango version : django-admin --version /n 
6) Create django project : enter to env_name folder and run this command (django-admin startproject portfolio_project) /n
7) Run the django project by entering the portfolio_project folder then entering : python3 mangr.py runserver /n
8) Create app in django project : python3 manage.py startapp mycv /n
9)-Create a templates folder inside the cv folder, and create a HTML file named mycv.html /n 
10)-Modify the view as following : /n
portfolio_project/students/views.py: /n
from django.http import HttpResponse /n
from django.template import loader /n

def Welcome(request): /n
template = loader.get_template('mycv.html') /n
return HttpResponse(template.render()) /n

11) Create file that named urls.py in app folder , and write in it as
following : /n
portfolio_project/students/urls.py: /n
from django.urls import path /n
from . import views /n

urlpatterns = [ 
path('Welcome/', views.Welcome, name='Welcome’),
] /n
12) Go to urls file in the project and write these : /n
portfolio_project/portfolio_project/urls.py: /n
from django.contrib import admin /n
from django.urls import include, path /n

urlpatterns = [
path('', include(‘mycv.urls')),
path('admin/', admin.site.urls),
] /n
13) Edit settings of the project as following :/n
portfolio_project/portfolio_project/settings.py:/n
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'mycv'
]/n
 
